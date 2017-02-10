''' An email sending script '''

import smtplib

from_name = 'Sender'
from_addr = 'username@gmail.com'
to_name = 'Recipient'
to_addr = 'person@email.com'
subject = 'Subject'
msg = 'Email message'
message = """From: {} <{}>
To: {} <{}>
Subject: {}


{}
"""
          
message_to_send = message.format(from_name, from_addr, to_name,
                                to_addr, subject, msg)

# Credentials (if needed)
username = 'username@gmail.com'
password = 'apppassword'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()