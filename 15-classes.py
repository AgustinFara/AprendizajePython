class Restaurant:

    def __init__(self):
        print("Me construyo con el constructor")

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #Atributo de clase Restaurant
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

class Banco:
    def __init__(self, nombre, origen, share):
        self.nombre = nombre #Atributo PUBLIC(default) de clase Banco asignado por el constructor
        self._origen = origen #Atributo PROTECTED de clase Banco asignado por el constructor
        self.__share = share #Atributo PRIVATE de clase Banco asignado por el constructor

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre} de {self._origen}, totaliza el {self.__share} del porcentaje de clientes de la Argentina')


    #GETTERS Y SETTERS

    def get_nombre(self):
        return self.nombre

    def get_origen(self):
        return self._origen

    def get_share(self):
        return self.__share

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_origen(self, origen):
        self._origen = origen

    def set_share(self, share):
        self.__share = share

#Herencia
class Hotel(Banco):
    def __init__(self, nombre, origen, share, estrellas):
        super().__init__(nombre, origen, share)
        self.__estrellas = estrellas    

    def set_estrellas(self,estrellas):
        self.__estrellas = estrellas
   
    def get_estrellas(self):
        return self.__estrellas

print('clase Restaurant objeto 1')
restaurant = Restaurant()
restaurant.agregar_restaurant('Spiagge di Napoli')
restaurant.mostrar_informacion() #accedo a atributo x método

print()
print('clase Restaurant objeto 2')
restaurant2 = Restaurant()
restaurant2.agregar_restaurant("McPython's")
restaurant2.mostrar_informacion() #acceder a atributo x método

print()
print('clase Banco objeto 1')
banco1 = Banco('Banco ITAU', 'Brasil', '12%')
banco1.mostrar_informacion() #acceder a atributo x método

print()
print('clase Banco objeto 2')
banco2 = Banco('Banco Macro','Argentina', '10%')
banco2.mostrar_informacion() #acceder a atributo x método



banco1.set_nombre('Banco Piano')        #Seteo por medio de metodos, buenas practicas, encapsulamiento
banco1.set_origen('Argentina')
banco1.set_share('7%')
print()
print('clase Banco objeto 1(Se cambiaron los atributos por medio de métodos)')
banco1.mostrar_informacion() #acceder a atributo x método

print()
print('clase Banco objeto 2(metodos get de atributos)')
print( banco2.get_nombre() )
print( banco2.get_origen() )
print( banco2.get_share() )

#Acceder sin método, mala práctica
print()
print('clase Restaurant accedida desde fuera del objeto(Atributos public)')
print(f"Mostrar: {restaurant.nombre}")
print(f"Mostrar: {restaurant2.nombre}")

print()
print('clase Hotel, herencia de clase Banco')

hotel1 = Hotel('Hyatt', 'USA', '2%', '*****')
hotel1.mostrar_informacion() #acceder a atributo x método

print()
print('clase Hotel, accedo a atributo nuevo clase hotel')
print(f'Hotel de {hotel1.get_estrellas()} estrellas')
