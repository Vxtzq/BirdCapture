from settings import *
if lang=="fr":
    initmessage = f"""\
                <html>
                    <head></head>
                    <body>
                        <h1> Bird Capture Init </h1>
                                    <h3> L'appareil a bien été initialisé ! </h3>
                                    <br><br>
                    </body>
                </html>
                """

if lang=="en":
    initmessage = f"""\
                <html>
                    <head></head>
                    <body>
                        <h1> Bird Capture Init </h1>
                                    <h3> The device has been initialized ! </h3>
                                    <br><br>
                    </body>
                </html>
                """
    
    

def message(log):
    
    birds = []
    if lang == "en":
        message = "List of birds detected since previous record :\n"
        birdslist = ""
        log = open(log, "r")
        lines = log.readlines()
        for line in lines:
            if not erasedate(line) in birds:
                birds.append(erasedate(line))
                birdslist = birdslist+erasedate(line)+"\n"
        messagestr = message
        html = f"""\
                <html>
                    <head>Bird Capture Report</head>
                    <body>
                        <h1></h1>
                        <h3> {messagestr} </h3>"""
        for name in birds:
            html = html+"""<br> {name}<br>""".format(name=name)
        html = html+"""</body>
                </html>
                """.format(messagestr=message,birdslist=birdslist)
  
                                    
                                                        
                
    if lang == "fr":
        message = "Liste des oiseau detectés depuis le précédent enregistrement (noms en anglais) :\n"
        birdslist = ""
        log = open(log, "r")
        lines = log.readlines()
        for line in lines:
            if not erasedate(line) in birds:
                birds.append(erasedate(line))
                birdslist = birdslist+erasedate(line)+"\n"
        messagestr = message
        html = f"""\
                <html>
                    <head>Bilan Bird Capture</head>
                    <body>
                        <h1></h1>
                        <h3> {messagestr} </h3>
                        """
        for name in birds:
            html = html+"""<br> {name}<br>""".format(name=name)
        html = html+"""</body>
                </html>
                """.format(messagestr=message,birdslist=birdslist)
                
    return message, html
def erasedate(string):
    output = string.replace(".","")
    output = output.replace("1","")
    output = output.replace("2","")
    output = output.replace("3","")
    output = output.replace("4","")
    output = output.replace("5","")
    output = output.replace("6","")
    output = output.replace("7","")
    output = output.replace("8","")
    output = output.replace("9","")
    output = output.replace("0","")
    output = output.replace("-","")
    output = output.replace(":","")
    output = output.replace(","," ")
    return output