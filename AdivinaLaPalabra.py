#Adivina la palabra

import random 

#Variables 
bancoDePalabras = ['perro', 'jirafa', 'enano', 'perimetro', 'murcielago', 'cuello', 'computadora', 'externo', 'planta']
palabra = random.choice(bancoDePalabras)  #Elige una palabra aleatoria de 'bancoDePalabras'
palabraAdivinar = ['_'] * len(palabra)    #Multiplica cada letra de la palabra para acultar las letras con un guión
intentos = 8

while intentos > 0:      
    
    print('n\Palabra actual: ' + ' '.join(palabraAdivinar) )
    
    adivinar = input('Elige una letra: ')
    
    if adivinar in palabra:
        for i in range(len(palabra)):        #Bucle para que recorra todas las letras de la palabra
            if palabra[i] == adivinar:       #Chequea si adivino la letra y en caso que sea asi, la revela
                palabraAdivinar[i] = adivinar
        print('Adivinaste!')
    else: 
        intentos -= 1        #Resta los intentos la no advinar la letra
        print('No adivinaste! Te quedan ' + str(intentos) + ' intentos')

    if '_' not in palabraAdivinar:
        print('Felicitaciones! Haz adivinado la palabra: ' + palabra)
        break
    else:
        print('Ya no tiene mas intentos! La palabra era: ' + palabra)
