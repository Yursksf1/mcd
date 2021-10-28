from tools import send_email_attachment

print('voy a enviar un email')

subject = "BONUS ZIRUS - Sanpedro "
sender = "bonos@zirus.com"
recipients = "test_zirus@mailinator.com"
bcc_recipients = []
text_body = "esto es una prueba"
html_body = "Esto es una <br> prueba"
path = "/Users/yurley.sanchez/Downloads/wetransfer-6d2f61"
name = "mac.jpg"
name_attachment = "bono_de_mac.jpg"

path_file = "{path}/{name}".format(path=path, name=name)
print(path_file)

send_email_attachment(
    subject,
    sender,
    recipients,
    text_body,
    html_body,
    bcc_recipients=bcc_recipients,
    file_path=path_file,
    report_name=name_attachment
)