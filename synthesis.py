import os
import matplotlib.pyplot as plt
from language import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import *
import smtplib, ssl
from base64 import b64encode
import io
from settings import *

def dofig(logcounter):
    global sendsynthesis
    if sendsynthesis == "true":
        birds = []
        birdscount = []
        logcount = logcounter
        run = True

        while run:
            if os.path.exists("logs/log"+str(logcount)+".log"):
                f = open("logs/log"+str(logcount)+".log","r")
                
                for line in f.readlines():
                    if not erasedate(line.replace("\n","")) in birds:
                        birds.append(erasedate(line.replace("\n","")))
                        birdscount.append(1)
                    else:
                        birdscount[birds.index(erasedate(line.replace("\n","")))] += 1
                logcount +=1
            else:
                run = False





        fig, ax = plt.subplots()
        fig.set_figheight(5)
        fig.set_figwidth(10)
        ax.pie(birdscount, labels=birds)
        port = 465 # For SSL
        smtp_server = smtpserver
        sender_email = str(address) 
        receiver_email = str(receiveremail)
        password = addresspassword
        img_format = 'png'


        fig = io.BytesIO()
        plt.savefig(fig, format=img_format,dpi=200)
        fig.seek(0)
        img_data = fig.read()
        if len(birds)> 0:
            if lang == "en":
                html = f'''<html>
                <head></head>
                <h1>BirdCapture synthesis</h1>
                <body>
                <img src="data:image/{img_format};base64, {b64encode(img_data).decode('ascii')}">
                </body>
                </html>'''
            if lang == "fr":
                html = f'''<html>
                <head></head>
                <h1>Synthèse BirdCapture</h1>
                <body>
                <img src="data:image/{img_format};base64, {b64encode(img_data).decode('ascii')}">
                </body>
                </html>'''
        else:
            if lang == "en":
                html = f'''<html>
                <head></head>
                <h1>BirdCapture synthesis</h1>
                <body>
                <br>No birds found, ensure the microphone is plugged in.</br>
                </body>
                </html>'''
            if lang == "fr":
                html = f'''<html>
                <head></head>
                <h1>Synthèse BirdCapture</h1>
                <body>
                <br>Aucun oiseau détecté, assurez vous que le micro de l'appareil est bien branché.</br>
                </body>
                </html>'''        
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["Subject"] = "birdcapture synthesis"
        msg["To"] = receiver_email

        part1 = MIMEText(html, 'html')
        msg.attach(part1)

        #msg.add_attachment(open(filename, "r").read(), filename=log)


        #add payload header with filename

        s = smtplib.SMTP_SSL(smtpserver, 465)
        s.ehlo()
        s.login(address, addresspassword)

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.send_message(msg)
        s.quit()
