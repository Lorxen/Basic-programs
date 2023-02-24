# Mail sender with python

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'your_email@gmail.com'
email_password = 'google_password'

email_reciever = 'reciever_email@gmail.com'

subject = 'SUBJECT OF THE MAIL'
body = '''
Body of the mail
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
