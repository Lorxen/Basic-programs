from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'brianylucia@gmail.com'
email_password = 'dbdnorwpoivndodu'

email_reciever = 'alissontorrez11@gmail.com'

subject = 'CORREO ENVIADO MEDIANTE CODIGO A MI AMOR'
body = '''
Hola mi vida como estas? yo me encuentro escribiendo codigo con 
dos manos y me soprende lo bien que me esta saliendo.

Un beso guapetona!
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
