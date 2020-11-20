import mysql.connector

from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the password
base_data = config_object["MySql"]

mydb = mysql.connector.connect(
  host=base_data["host"],
  user=base_data["user"],
  password=base_data["password"],
  database=base_data["database"]
)

nombre = input("que tabla quiere consultar?: \r\n") 

mycursor = mydb.cursor()

mycursor.execute(f"SELECT * FROM {nombre}")

for x in mycursor:
  print(x)