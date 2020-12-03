import os
import platform
import datetime
import sys
import msvcrt

#CONSTANTES
CWD = os.path.dirname(os.path.realpath(__file__)) #busco directorio del script (Current Work Directory)
CARPETA = CWD + '\contactos\\' #Carpeta de trabajo + Carpeta contactos
EXTENSION = ".txt" #extensión para los archivos generados

#Clases
class Contacto:
    def __init__(self, nombre, telefono, cumpleaños):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__cumpleaños = cumpleaños


    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_cumpleaños(self):
        return self.__cumpleaños

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_origen(self, telefono):
        self.__telefono = telefono

    def set_cumpleaños(self, cumpleaños):
        self.__cumpleaños = cumpleaños
    
# Crea el directorio de contactos si no existe
def genera_dir():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

#Limpia la pantalla de la consola
def limpia_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#Muestra Menu Principal
def mostrar_menu():
    print("Indique la opción deseada")
    print("------- -- ------ -------")
    print()
    print("1 - Agregar nuevo Contacto")
    print("2 - Editar contacto")
    print("3 - Ver contactos")
    print("4 - Buscar contacto")
    print("5 - Eliminar contacto")
    print("6 - Salir")
    print()

#Lógica de selección de operación 
def lee_opcion():
    preguntar = True
    while preguntar:
        opcion = input("Ingrese el número deseado: ")
        #verifica que se ingrese un numero, si no puede ser convertido a int, no entra en las opciones del if y vuelve a preguntar
        try:
            opcion = int(opcion)
        except:
            pass

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            valida_editar_contacto()
            preguntar = False
        elif opcion == 3:
            listar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            borrar_contacto_valida()
            preguntar = False
        elif opcion == 6:
            aviso_salida()
            limpia_pantalla()
            preguntar = False
        else:
            pantalla_inicial()

#Pantalla Agregar Contacto
def agregar_contacto():
    #seteo booleanos de verificación de carga de cada item
    nombre_cargado = False
    telefono_cargado = False
    cumpleaños_cargado = False
    
    #loop hasta poder validar todos los campos, reseteando la pantalla
    while not (nombre_cargado and telefono_cargado and cumpleaños_cargado):   
        limpia_pantalla()
        
        print("Ingrese los datos del nuevo Contacto")
        print("------- --- ----- --- ----- --------")
        
        #Pide el nombre del contacto si ya fue cargado lo muestra
        if nombre_cargado == False:
            nombre_contacto = input("Nombre completo: ")
            nombre_cargado = True
        else:
            print("Nombre completo: " + nombre_contacto)
        
        #Pide el teléfono del contacto si ya fue cargado lo muestra
        if telefono_cargado == False:
            telefono_contacto = input("Teléfono: ")
            telefono_cargado = True
        else:
            print("Teléfono: " + telefono_contacto)
        

        cumpleaños_contacto = input("Ingrese una fecha de cumpleaños formato AAAA.MM.DD: ")

        #Pide el cumpleaños del contacto, verifica fecha válida al transformarlo a date       
        try:
            año, mes, dia = map(int, cumpleaños_contacto.split("."))
            cumpleaños_contacto_date = datetime.date(año, mes, dia)
            cumpleaños_cargado = True
        except:
            pass
            

    #Al tener todos los datos instancio contacto nuevo
    contacto = Contacto(nombre_contacto.upper(),telefono_contacto,cumpleaños_contacto_date)
    
    #verifico que no exista antes de grabarlo
    if not existe_contacto( nombre_contacto.upper() ):

        #Grabo el contacto en un archivo nuevo
        with open(CARPETA + nombre_contacto.upper() + EXTENSION, "w") as archivo:
            archivo.write(contacto.get_nombre() + "/")
            archivo.write(contacto.get_telefono() + "/" )
            archivo.write(contacto.get_cumpleaños().strftime("%d/%m/%Y") )
        aviso_contacto_agregado(contacto.get_nombre())
    else:
        aviso_contacto_existente(contacto.get_nombre())

#Pantalla Validar Editar Contacto
def valida_editar_contacto():
    limpia_pantalla()
    print("Ingrese los datos del  Contacto a Editar")
    print("------- --- ----- ---  -------- - ------")
    nombre_contacto = input("Nombre completo: ")
    #valida si existe o no para editar el contacto
    if existe_contacto(nombre_contacto):
        editar_contacto(nombre_contacto)
    else:
        aviso_contacto_inexistente(nombre_contacto)

#Pantalla Editar Contacto
def editar_contacto(nombre):
    limpia_pantalla()

    #abro archivo a editar
    with open(CARPETA + nombre.upper() + EXTENSION, "r") as archivo:
        nom, tel, año, mes, dia = map(str, archivo.readline().split("/"))
    
    #pido los nuevos datos
    nombre_contacto = editar_nombre(nom)
    telefono_contacto = editar_telefono(tel)
    cumpleaños_contacto = editar_cumpleaños(año + "/" + mes + "/" + dia)

    if nombre_contacto.upper() == nombre.upper():
        pass
    else:
        os.rename(CARPETA + nombre.upper() + EXTENSION, CARPETA + nombre_contacto.upper() + EXTENSION)
    
    with open(CARPETA + nombre_contacto.upper() + EXTENSION, "w") as archivo:
        archivo.write(nombre_contacto.upper() + "/")
        archivo.write(telefono_contacto + "/" )
        archivo.write(cumpleaños_contacto.strftime("%d/%m/%Y") )
    aviso_contacto_modificado(nombre_contacto)

#Pantalla para editar nombre        
def editar_nombre(nombre):
    limpia_pantalla()
    print("PRESIONE ENTER SI DESEA MANTENER EL DATO GUARDADO")
    nom_contacto = input(f"Nombre completo({nombre.title()}), escriba el nuevo: ")
    if(len(nom_contacto) == 0):
        nom_contacto = nombre
        
    return nom_contacto  

#Pantalla para editar telefono
def editar_telefono(telefono):
    limpia_pantalla()
    print("PRESIONE ENTER SI DESEA MANTENER EL DATO GUARDADO")
    tel_contacto = input(f"Teléfono({telefono}), escriba el nuevo: ")
    if(len(tel_contacto) == 0):
       tel_contacto = telefono

    return tel_contacto

#pantalla para editar cumpleaños
def editar_cumpleaños(cumpleaños):
    cum_cargado = False
    while not cum_cargado:
        limpia_pantalla()
        print("PRESIONE ENTER SI DESEA MANTENER EL DATO GUARDADO")
        cum_contacto = input(f"Cumpleaños({cumpleaños}), escriba el nuevo AAAA.MM.DD: ")
        if(len(cum_contacto) == 0):
            dia, mes, año = map(int, cumpleaños.split("/"))
            cum_contacto_date = datetime.date(año, mes, dia)
            cum_cargado = True
        else:
            try:
                año, mes, dia = map(int, cum_contacto.split("."))
                cum_contacto_date = datetime.date(año, mes, dia)
                cum_cargado = True
            except:
                pass
    
    return cum_contacto_date

#Pantalla que lista los contactos
def listar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_ext_valida = [i for i in archivos if i.endswith(EXTENSION)]

    for elemento in archivos_ext_valida:
        with open(CARPETA + elemento, "r") as archivo:
            nom, tel, año, mes, dia = map(str, archivo.readline().split("/"))
        limpia_pantalla()
        print(nom.title())
        print(convertir_subrayado(nom))
        print("Teléfono: " + tel)
        print("Cumpleaños: " + año + "/" + mes + "/" + dia)
        print()
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        
    
    inicializa_aplicación(False)

#Pantalla de busqueda de contacto  
def buscar_contacto():
    limpia_pantalla()
    print("Ingrese los datos del  Contacto a Buscar")
    print("------- --- ----- ---  -------- - ------")
    nombre_contacto = input("Nombre completo: ")
    if existe_contacto(nombre_contacto):
        mostrar_contacto(nombre_contacto)
    else:
        aviso_contacto_inexistente(nombre_contacto)        

#Verifica que el elemento a borrar exista
def borrar_contacto_valida():
    limpia_pantalla()
    print("Ingrese los datos del  Contacto a Borrar")
    print("------- --- ----- ---  -------- - ------")
    nombre_contacto = input("Nombre completo: ")
    if existe_contacto(nombre_contacto):
        borrar_contacto(nombre_contacto)
    else:
        aviso_contacto_inexistente(nombre_contacto)  

#Pantalla de borrado
def borrar_contacto(elemento):
    limpia_pantalla()
    with open(CARPETA + elemento.upper() + EXTENSION, "r") as archivo:
        nom, tel, año, mes, dia = map(str, archivo.readline().split("/"))
    limpia_pantalla()
    print(nom.title())
    print(convertir_subrayado(nom))
    print("Teléfono: " + tel)
    print("Cumpleaños: " + año + "/" + mes + "/" + dia)
    print()

    confirma = input("Esta seguro que desea eliminar este contacto? S o N: ")
    if confirma.upper() == 'S':
        os.remove(CARPETA + elemento.upper() + EXTENSION)
        borro(elemento)
    else:
        no_borro(elemento)
      
#Muestra un contacto especifico
def mostrar_contacto(nombre_contacto):
    with open(CARPETA + nombre_contacto + EXTENSION, "r") as archivo:
        nom, tel, año, mes, dia = map(str, archivo.readline().split("/"))
    limpia_pantalla()
    print(nom.title())
    print(convertir_subrayado(nom))
    print("Teléfono: " + tel)
    print("Cumpleaños: " + año + "/" + mes + "/" + dia)
    print()
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

# Genera subrayado para un string   
def convertir_subrayado(texto):
    for x in range(0,len(texto)):
        if not texto[x] == ' ':
            texto = texto[:x] + '-' + texto[(x + 1):] 
        
    return texto

# Consulta si existe contacto
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre.upper() + EXTENSION)

#pantalla de aviso contacto agregado
def aviso_contacto_agregado(nombre):
    limpia_pantalla()
    print(f"El contacto: {nombre.title()} se guardo correctamente")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

#Pantalla de aviso contacto modificado
def aviso_contacto_modificado(nombre):
    limpia_pantalla()
    print(f"El contacto: {nombre} se modificó correctamente")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

#Pantalla de aviso contacto existente
def aviso_contacto_existente(nombre):
    limpia_pantalla()
    print(f"El contacto: {nombre} ya existe, no puede ser añadido ")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

#Pantalla de aviso contacto eliminado
def borro(nombre):
    limpia_pantalla()
    print(f"El contacto: {nombre} fue eliminado")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

#Pantalla de aviso contacto no eliminado
def no_borro(nombre):
    limpia_pantalla()
    print(f"El contacto: {nombre} no fue borrado ")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

#Pantalla de aviso contacto inexistente
def aviso_contacto_inexistente(nombre):
    limpia_pantalla()
    print(f"El contacto: {nombre} no existe, crear el contacto primero ")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    inicializa_aplicación(False)

#Pantalla de salida aplicación
def aviso_salida():
    limpia_pantalla()
    print(f"Saliendo de la aplicación")
    print("Presione una tecla para continuar...")
    msvcrt.getch()

#Muestra Pantalla principal
def pantalla_inicial():
    limpia_pantalla()
    mostrar_menu()

#Inicializa aplicacion, si se le envia true de parametro intenta generar directorio
def inicializa_aplicación(genera_directorio):
    if genera_directorio:
        genera_dir()
    else:
        pass
    pantalla_inicial()
    lee_opcion()

#llamada a ejecución de la aplicación
inicializa_aplicación(True)


