def grabar():

    archivo = open("Archivo.txt", "w") #Escritura, si no existe lo crea

    for i in range(1,21):
        archivo.write("Esta es la linea: " + str(i) + "\r")


    archivo.close()

def leer():
    with open("Archivo.txt") as archivo: # cierra automaticamente de esta forma
        for contenido in archivo:
            print(contenido.rstrip())

grabar()

leer()

