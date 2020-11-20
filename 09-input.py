
nombre = input("Cual es tu nombre: \r\n")

print(f"¡Hola {nombre}!")

edad = input(f"{nombre}, ¿Cual es tu edad?: \r\n")

try:
    edad = int(edad)

    if edad >= 18:
        print(f"{nombre}, ya puedes votar")
    else:
        print(f"{nombre}, aún no puedes votar")


except:
    print("La edad que ingresó debe ser numérica")

dia_nacimiento = input(f"{nombre}, ¿Cual es tu día de nacimiento?: \r\n")

try:
    dia_nacimiento = int(dia_nacimiento)

    if dia_nacimiento % 2 == 0:
        print(f"{nombre}, tu día de nacimiento es par")
    else:
        print(f"{nombre}, tu día de nacimiento es inpar")
except:
    print("El día de nacimiento debe ser numérico")




