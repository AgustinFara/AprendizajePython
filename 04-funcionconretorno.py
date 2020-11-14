#definición función porcentaje
def porcentaje(parte,total):
    return((100 * parte) /total )
#definición función valor dólar
def valor_dolar_solidario(pesos,cotización):
    return(pesos * cotización * 1.30 * 1.30)

#llamado a funciones de  ejemplo
print(f' {porcentaje(195,200)} %')

print(f' {porcentaje(250,500)} %')

print(f' {porcentaje(127.81,7600.23)} %')

print(f' {valor_dolar_solidario(200,84)}Usd$')

# calculo exponencial
print(3**3)

# suma ++ en python
numero = 5
numero += 1
print(numero)