import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Mahedi Hassan'
email['to'] = 'erroerror80@gmail.com'
email['subject'] = 'You won 1,0000000 dollars!'


email.set_content(html.substitute({'name': 'Leah'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dumtum02@gmail.com', '#20dtum@')
    smtp.send_message(email)
    print('Everything is ok!')
