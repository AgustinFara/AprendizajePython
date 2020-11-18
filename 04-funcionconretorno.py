#definición función porcentaje
def porcentaje(parte,total):
    return((100 * parte) /total )
#definición función valor dólar
def valor_dolar_solidario(pesos,cotización):
    #calculo de cotizacion más retención x impuesto país más retencion del 35%
    return(pesos * cotización + (pesos * cotización * 0.30) + (pesos * cotización * 0.35))

#llamado a funciones de  ejemplo
print(f' {porcentaje(195,200)} %')

print(f' {porcentaje(250,500)} %')

print(f' {porcentaje(127.81,7600.23)} %')

print(f' {valor_dolar_solidario(200,84.60)}Usd$')

# calculo exponencial
print(3**3)

# suma ++ en python
numero = 5
print(numero)
numero += 1
print(numero)