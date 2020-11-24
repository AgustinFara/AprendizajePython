import requests
import json

isbn_13 = input("ingrese un ISBN 13: \r\n")

url = str(f"http://openlibrary.org/query.json?type=/type/edition&isbn_13={isbn_13}&books=")

try:
    resp = requests.get(url)

    if int(resp.status_code) == 200:
        #Genero un diccionario con la respuesta en Json
        json_to_dics = json.loads(resp.content)
        #Busco el numero de pagina corresponiente a la busqueda
        clave_open_library = (json_to_dics[0]["key"])

    else:
        print("error al comunicarse con Open Library")
except:
    print("error al llamar a la API")

url = str(f"http://openlibrary.org{clave_open_library}.json")

try:
    resp = requests.get(url)

    if int(resp.status_code) == 200:
        #Genero un diccionario con la respuesta en Json
        json_to_dics = json.loads(resp.content)
        
        #muestro datos
        if "title" in json_to_dics: 
            print(json_to_dics["title"])

        if "by_statement" in json_to_dics:
            print(json_to_dics["by_statement"])

        if "publishers" in json_to_dics:
            print(json_to_dics["publishers"])

        if "number_of_pages" in json_to_dics:    
            print(json_to_dics["number_of_pages"])

        if "publish_date" in json_to_dics:        
            print(json_to_dics["publish_date"])

        if "publish_country" in json_to_dics:    
            print(json_to_dics["publish_country"])

        if "publish_places" in json_to_dics:       
            print(json_to_dics["publish_places"])
        
        if "isbn_10" in json_to_dics:       
            print(json_to_dics["isbn_10"])

        if "isbn_13" in json_to_dics:       
            print(json_to_dics["isbn_13"])

    else:
        print("error al comunicarse con Open Library")
except:
    print("error al llamar a la API")




