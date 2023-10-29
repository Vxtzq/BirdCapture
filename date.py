from datetime import date
import datetime
 
# Returns the current local date
def getDate():
    today = datetime.datetime.now()
    year = str(today)
    year = year[:4]
    month = str(today)
    month = month[5:7]
    day = str(today)
    day = day[8:10]
    
    day = day.replace(" ","")
    time = str(today)
    time = time[11:19]
    
    return int(year), int(month), int(day),today,time

