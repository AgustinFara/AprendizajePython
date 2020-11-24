import smtplib 

from configparser import ConfigParser

#Leo config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Tomar los datos de Servidor SMTP del config.ini
smtp_data = config_object["SMTP"]
host = smtp_data["host"]
port = smtp_data["port"]
user = smtp_data["user"]
password = smtp_data["password"]


remitente = "Private Person <from@smtp.smtpman.com>" 
destinatario = "A Test User <to@smtp.smtpman.com>" 
asunto = "Email HTML enviado desde Python" 
mensaje = """Hola!<br/> <br/> 
Este es un <b>e-mail</b> enviando desde <b>Python</b> 
"""

email = """From: %s 
To: %s 
MIME-Version: 1.0 
Content-type: text/html 
Subject: %s 

%s
""" % (remitente, destinatario, asunto, mensaje) 


try: 
    with smtplib.SMTP(host,port) as server:
        server.login(user,password)
        server.sendmail(remitente, destinatario, email) 
    print("Correo enviado") 
except: 
    print("""Error: el mensaje no pudo enviarse. Compruebe su conexión de internet""")