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
with open('config.ini', 'w') as conf: # w es permisos de escritura, si no existe lo crea.
    config_object.write(conf)