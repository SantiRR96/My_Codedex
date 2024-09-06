#Convertidor de N° romanos

ingresoNumero = input('Ingrese el numero romano que quiere saber: ')

def romano_a_entero(numero):
    
    respuestaFinal = 0

    if 'CM' in numero:
        respuestaFinal += 900
        numero = numero.replace('CM', '')
    if 'CD' in numero:
        respuestaFinal += 400
        numero = numero.replace('CD', '')
    if 'XC' in numero:
        respuestaFinal += 90
        numero = numero.replace('XC', '')
    if 'XL' in numero:
        respuestaFinal += 40
        numero = numero.replace('XL', '')
    if 'IX' in numero:
        respuestaFinal += 9
        numero = numero.replace('IX', '')
    if 'IV' in numero:
        respuestaFinal += 4
        numero = numero.replace('IV', '') #Valuo casos especiales fuera del diccionario general

    for i in numero:
        if i == 'M':
            respuestaFinal += 1000
        elif i == 'D':
            respuestaFinal += 500
        elif i == 'C':
            respuestaFinal += 100
        elif i == 'L':
            respuestaFinal += 50
        elif i == 'X':
            respuestaFinal += 10
        elif i == 'V':
            respuestaFinal += 5
        elif i == 'I':
            respuestaFinal += 1   #Diccionario de valores 
    
    print('El numero romano que ingresaste es: ' + str(respuestaFinal))

romano_a_entero(ingresoNumero)
