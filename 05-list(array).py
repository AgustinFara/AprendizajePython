#Dos list para stock de películas Videoclub
Peliculas = ["Volver al Futuro I", "Tiburón", "Jurassic Park", "Matilda", "Indiana Jones y los Cazadores del arca perdida", "Batman Vuelve"]
Stock = [True, False,True,True,False,True]

#Recorro los dos list para mostrar por consola las películas alquiladas
print ("STOCK")
for x in range(len(Peliculas)):
    if Stock[x] == True:
        print(f"{Peliculas[x]} :  en stock")
    else:
        print(f"{Peliculas[x]} :  alquilada")


# Elimino Pelicula Matilda y su flag de alquilada
Peliculas.pop(3) # .pop() vacio elimina el último elemento
Stock.pop(3)

#Recorro Nuevamente sin Matilda
print() #Espaciado para dividir con el listado previo
print ("STOCK")
for x in (0,1,2,3,4,): #quito un elemento
    if Stock[x] == True:
        print(f"{Peliculas[x]} :  en stock")
    else:
        print(f"{Peliculas[x]} :  alquilada")

#Sorteo list Películas
Peliculas.sort()

#Elimino por nombre
Peliculas.remove("Tiburón")


#Listado de Peliculas Sorteado
print() #Espaciado para dividir con el listado previo
print("TOTAL DE PELICULAS")
for x in Peliculas:
    print(x)
