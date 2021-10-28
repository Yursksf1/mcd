
from threading import Thread
import os.path
import smtplib
from flask.ext.mail import Message

from loanservice.default_config import REPORTS_PATH

from notificationservice.app import app, mail
from notificationservice.app.config import ENABLE_SECONDARY_SMTP_SERVER, MAIL_SERVER_SECONDARY, MAIL_PORT_SECONDARY
from notificationservice.util.log_config import logger

JSON_HEADERS = {'Content-Type': 'application/json'}


def headers():
    return JSON_HEADERS


def send_async_email(msg):
    with app.app_context():
        mail.send(msg)

def __send_email_by_secondary_smtp(subject, sender, recipients, text_body, html_body):
    """
    Send an email to a secondary smtp server(for debug or automation prupose) if it's enabled.
    :param subject: String, Email's subject. Ie, "Hello"
    :param sender: String, Email from sender. Ie, "arosero@lendingfront.com"
    :param recipients: String, Destination emails. Ie, "jenkins@lendingfront.com, technology@lendingfront.com"
    :param text_body: String, Content of the email in plain text. Ie, "This is the email content."
    :param html_body: String, Content of the email in html. Ie, "<p>This is the email content.</p>"
    """

    if (ENABLE_SECONDARY_SMTP_SERVER.lower() != 'true'):
        return

    server = smtplib.SMTP(MAIL_SERVER_SECONDARY, MAIL_PORT_SECONDARY)
    msg = 'Subject: {}\n\n{}'.format(subject, text_body + html_body )
    thread = Thread(target=server.sendmail, args=[sender, recipients, msg])
    thread.start()

def send_email(subject, sender, recipients, text_body, html_body, bcc_recipients=None, cc_recipients=None,
               file_path=None, report_name=None):
    """
    Send an email by main smtp server. It also send the mail through a secondary smtp server if it's enabled.
    :param subject: String, Email's subject. Ie, "Hello"
    :param sender: String, Email from sender. Ie, "arosero@lendingfront.com"
    :param recipients: String, Destination emails. Ie, "jenkins@lendingfront.com, technology@lendingfront.com"
    :param text_body: String, Content of the email in plain text. Ie, "This is the email content."
    :param html_body: String, Content of the email in html. Ie, "<p>This is the email content.</p>"
    :param bcc_recipients: String, Blind carbon copy email list. Ie, "jenkins@lendingfront.com, technology@lendingfront.com"
    :param cc_recipients: String, Carbon copy email list. Ie, "jenkins@lendingfront.com, technology@lendingfront.com"
    """
    if file_path:
        send_email_attachment(subject, sender, recipients, text_body, html_body, bcc_recipients=bcc_recipients,
                              file_path=file_path, report_name=report_name)
        return

    __send_email_by_secondary_smtp(subject, sender, recipients, text_body, html_body)
    msg = Message(
        subject, sender=sender, recipients=recipients,
        bcc=bcc_recipients,
        cc=cc_recipients
    )
    msg.body = text_body
    msg.html = html_body
    thread = Thread(target=send_async_email, args=[msg])
    thread.start()


def send_returned_payments_email(subject, sender, recipients, text_body, html_body, report_name, bcc_recipients=None):

    file_path = os.sep.join((REPORTS_PATH, report_name))

    send_email_attachment(subject, sender, recipients, text_body, html_body, report_name, file_path, bcc_recipients)


def send_email_pdf_report(subject, sender, recipients, text_body, html_body, report_name, bcc_recipients=None):
    file_path = os.sep.join((REPORTS_PATH, report_name))
    send_email_attachment(subject, sender, recipients, text_body, html_body, report_name, file_path, bcc_recipients)


def send_email_attachment(subject, sender, recipients, text_body, html_body, report_name, file_path,
                          bcc_recipients=None, raise_exception=False):

    __send_email_by_secondary_smtp(subject, sender, recipients, text_body, html_body)
    msg = Message(subject, sender=sender, recipients=recipients, bcc=bcc_recipients)

    msg.body = text_body
    msg.html = html_body

    if file_path and os.path.exists(file_path):

        mime_attachment_type = get_file_mime_type(file_path=file_path)
        with app.open_resource(file_path) as fp:
            msg.attach(file_path, mime_attachment_type, fp.read())

        attachment = msg.attachments[0]
        attachment.filename = report_name

        thread = Thread(target=send_async_email, args=[msg])
        thread.start()
    else:
        err_msg = "File: {0} does not exist. Returned Payments Email not sent".format(file_path)
        logger.warn(err_msg)
        if raise_exception:
            raise Exception(err_msg)


def get_file_mime_type(file_path):
    """
    Get the mime type for add to the attachment email header.
    :param file_path: String, file path that contains the file extension.
    :return: String file mime type for the attachment, Ie "application/pdf".
    """

    file_extension = file_path.split('.')[-1]
    mime_attachment_type = "text/xls"
    if file_extension.lower() == "pdf":
        mime_attachment_type = "application/pdf"

    return mime_attachment_type

