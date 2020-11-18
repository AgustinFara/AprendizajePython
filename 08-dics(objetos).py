cancion = {
    "artista" : "Metallica", #Llave y valor
    "nombre" : "Enter Sandman",
    "album"   : "Black Album",
    "año de Lanzamiento" : 1992
}

#Acceder los datos del diccionario
print(cancion["artista"])
print(cancion["nombre"])
print(cancion["album"])
print(cancion["año de Lanzamiento"])

#Agregar valores
cancion["genero"] = "Heavy Metal"

#imprimo todo para verificar
print(cancion)

#cambio valores
cancion["nombre"] = "Nothing else Matters"

#imprimo todo para verificar
print(cancion)

#imprimo atributo genero
print(cancion.get("genero", "No existe el Valor"))

#elimino valor del diccionario
del cancion["genero"]

#imprimo atributo genero
print(cancion.get("genero", "No existe el Valor"))

print() #linea vacía
print("VALORES CANCIÓN")
#Recorro el diccionario
for llave, valor in cancion.items():
    print(f"{llave} : {valor}")




