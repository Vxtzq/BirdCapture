from settings import *
import smtplib, ssl
from language import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path




def sendInitMail():
    global initmessage, sendinit
    if sendinit=="true":
        port = 465 # For SSL
        smtp_server = "smtp.free.fr"
        sender_email = "pierre.elger@free.fr"  # Enter your address
        receiver_email = str(address)  # Enter receiver address
        password = addresspassword
        initmsg = MIMEMultipart()
        initmsg["From"] = sender_email
        initmsg["Subject"] = "birdcapture init"
        initmsg["To"] = receiver_email
        
        part1 = MIMEText(initmessage, 'html')
        initmsg.attach(part1)
        s = smtplib.SMTP_SSL(smtpserver, 465)
        s.ehlo()
        s.login(address, addresspassword)

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.send_message(initmsg)
        s.quit()

    
def sendMail(log):
    global message,receiveremail,smtpserver,address,addresspassword,sendinfo,sendlogs
    
    if sendinfo=="true":
        
        if sendlogs=="true":
            
            port = 465 # For SSL
            smtp_server = smtpserver
            sender_email = str(address)  # Enter your address
            receiver_email = str(receiveremail)  # Enter receiver address
            password = addresspassword
            
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["Subject"] = "birdcapture"
            msg["To"] = receiver_email
            mailmessage, html = message(log)
            part1 = MIMEText(html, 'html')
            msg.attach(part1)
            filename=log
            #msg.add_attachment(open(filename, "r").read(), filename=log)
            
            attach_file = open(log, 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) #encode the attachment
            #add payload header with filename
            payload.add_header('Content-Disposition', 'attachment', filename=log)
            msg.attach(payload)
            print(receiveremail)
            s = smtplib.SMTP_SSL(smtpserver, 465)
            s.ehlo()
            s.login(address, addresspassword)

            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
            s.send_message(msg)
            s.quit()
        else:
            port = 465 # For SSL
            smtp_server = smtpserver
            sender_email = str(address)  # Enter your address
            receiver_email = str(receiveremail)  # Enter receiver address
            password = addresspassword
            
            
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["Subject"] = "birdcapture"
            msg["To"] = receiver_email
            mailmessage, html = message(log)
            part1 = MIMEText(html, 'html')
            msg.attach(part1)
            

            s = smtplib.SMTP_SSL(smtpserver, 465)
            s.ehlo()
            s.login(address, addresspassword)

            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
            s.send_message(msg)
            s.quit()
