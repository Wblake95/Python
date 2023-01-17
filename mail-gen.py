from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Creat_Email():
    msg             = MIMEMultipart('alternative')
    msg['Subject']  = 'My Subject'
    msg['To']       = 'test@gmail.com'

    text = 'this is sample text'

    part = MIMEText(text, 'text')
    msg.attach(part)

    outfile_name = r'email-sample.eml'
    with open(outfile_name, 'w') as outfile:
        gen = generator.Generator(outfile)
        gen.flatten(msg)

Creat_Email()
