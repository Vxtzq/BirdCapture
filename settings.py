import configparser

configParser = configparser.RawConfigParser()   
configFilePath = 'config.cfg'
configParser.read(configFilePath)
lang = configParser.get("general","language")
saverecords = configParser.get("record","save_record_files")
savelogs = configParser.get("general","save_logs")
sendlogs = configParser.get("mail","send_logs")
lattitude = configParser.get("general","lattitude")
longitude = configParser.get("general","longitude")
recordlength = configParser.get("record","record_length")
record_filename = configParser.get("record","record_filename")
