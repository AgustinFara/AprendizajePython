from configparser import ConfigParser

#asigno al objeto configparser
config_object = ConfigParser()

#Agrego sección de base MySQL
config_object["MySql"] = {
    "host": "myhost",
    "user": "myUSER",
    "password": "mypassword",
    "database": "myschema",
}

#Genero el archivo config.ini
with open('config.ini', 'w') as conf:
    config_object.write(conf)