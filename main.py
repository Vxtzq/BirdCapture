from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import os
from mic import *
from date import getDate
from mail import *
import time
from threading import Thread
from language import *
from email.mime.base import MIMEBase

sendInitMail()
# Load and initialize the BirdNET-Analyzer models.

logcount = 0
detections = []
def main():
    global logcount,detections, timebetween
    analyzer = Analyzer()
    
    while True:
        currentyear, currentmonth, currentday, date,hour = getDate()
        recording = Recording(
            analyzer,
            record(),
            lat=43.2598,
            lon=0.971861,
            date=datetime(year=currentyear, month=currentmonth, day=currentday), # use date or week_48
            min_conf=0.25,
        )
        
        recording.analyze()
        print(recording.detections)


        
        logcount +=1
        if not os.path.exists("logs/log"+str(logcount)+".log"):
            
            log = open("logs/log"+str(logcount)+".log", "x")
            log.close()
            
           
        log = open("logs/log"+str(logcount)+".log", "a")
        
        for detect in recording.detections:
            if not detect['common_name']+" ,("+str(detect['scientific_name'])+")" in detections:
                detections.append(detect['common_name']+" ,("+str(detect['scientific_name'])+")")
            log.write(str(detect['common_name']+",("+str(detect['scientific_name'])+"),"+str(detect['confidence']))+","+str(date)+"\n")
        log.close()
        
        print("detections : "+str(detections))
        print("waiting for "+timebetween+" seconds...")
        time.sleep(int(timebetween))
def Mail():
    global detections,logcount
    while True:
        time.sleep(int(infointerval)*60)
        if os.path.exists("logs/log"+str(logcount)+".log"):
            sendMail("logs/log"+str(logcount)+".log")
        else:
            sendMail("logs/log"+str(logcount-1)+".log")
        
t1 = Thread(target=main)
t2 = Thread(target=Mail)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()
