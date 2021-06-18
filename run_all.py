# -*- coding: utf-8 -*-

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from local_data import information, datas, html as html_base, text as text_base
from string import Template


def sent_mail(email, name, url):

    username = information.get('username')
    password = information.get('password')

    send_from = username
    subject = "Bono Ziru's Pizza 🍕 Col. San Pedro 🎁"

    print('voy a enviar un email a: {} {} {}'.format(email, name, url))

    send_to = [email]

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = subject

    text = text_base.format(name=name, url=url)
    text = " "
    html = Template(html_base).substitute(name=name, url=url)

    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    smtp = smtplib.SMTP(host="smtp.gmail.com", port = 587)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    print(' se envio el email')
    print('')

def run_script():
    contador = 0
    for data in datas:
        print('{}: preparando data para enviar el email {}'.format(contador, data))
        contador = contador + 1

        time.sleep(1)
        email = data[0]
        name = data[1]
        name = name.split(' ')[-1]
        url = data[2]

        sent_mail(
            email=email,
            name=name,
            url=url
        )


if __name__ == "__main__":
    run_script()