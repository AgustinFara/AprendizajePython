import requests
import json

#from requests.structures import CaseInsensitiveDict

url = "https://es.wikipedia.org/w/api.php?format=json&origin=*&action=query&prop=extracts&explaintext=false&exintro&titles=Jorge+Luis+Borges"

try:
    resp = requests.get(url)

    if int(resp.status_code) == 200:
        #Genero un diccionario con la respuesta en Json
        json_to_dics = json.loads(resp.content)
        #Busco el numero de pagina corresponiente a la busqueda
        page_num_obj = list(json_to_dics["query"]["pages"].keys())[0]
        page_num = str(page_num_obj)
        #Accedo al extracto y lo imprimo
        print(json_to_dics["query"]["pages"][page_num]["extract"])
    else:
        print("error al comunicarse con Wikipedia")
except:
    print("error al llamar a la API")



