#evaluación numerica
billetera = 2

if billetera >= 10:
    print("tienes saldo para comprar el turrón")
else:
    print("no tienes saldo para comprar el turrón")

#evaluación texto
lenguaje = "Python"

if lenguaje == "Python":
    print(f"Excelente")

#evaluación bool
usuario_autenticado = True


if usuario_autenticado:
    print("Puede acceder al sistema")
else:
    print("Debes iniciar sesión")

#evaluacion de elemento en lista

frutas = ["Ananá", "Banana", "Pera", "Kiwi", "Manzana"]

if "Naranja" in frutas:
    print("Naranja en stock")
else:
    print("No hay naranjas")

#if anidado

justice_league = True
batman_v_superman = True

if justice_league:
    if batman_v_superman:
        print("viste ambas películas")
    else:
        print("Solo viste Justice League")
else:
    if batman_v_superman:
        print("Solo viste Batman v Superman")
    else:
        print("No viste ninguna de las dos")

#Lo mismo con elif y and

if justice_league and batman_v_superman:
    print("viste ambas películas")
elif justice_league and batman_v_superman == False:
    print("Solo viste Justice League")
elif justice_league == False and batman_v_superman:
    print("Solo viste Batman v Superman")
else:
    print("No viste ninguna de las dos")



#Uso del elif
puntuacion = 1

if puntuacion <= 3:
    print("Insuficiente")
elif puntuacion <= 6:
    print("Regular")
elif puntuacion == 7:
    print("Bueno")
elif puntuacion <= 9:
    print("Muy bueno")
elif puntuacion == 10:
    print("Sobresaliente")
else:
    print("número de puntuación incorrecto")
