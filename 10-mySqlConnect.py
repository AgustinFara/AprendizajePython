import mysql.connector

from configparser import ConfigParser

#Leo config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Tomar los datos de MySQl del config.ini
base_data = config_object["MySql"]

mydb = mysql.connector.connect(
  host=base_data["host"],
  user=base_data["user"],
  password=base_data["password"],
  database=base_data["database"]
)

seguir_consultando = True

while seguir_consultando:
  
  nombre = input("que tabla quiere consultar?: \r\n")

  mycursor = mydb.cursor()
  if nombre == "cerrar":
    seguir_consultando = False
  else:
    mycursor.execute(f"SELECT * FROM {nombre}")
    for x in mycursor:
      print(x)