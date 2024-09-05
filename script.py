# Contadores para cada casa
contadorG = 0  # Gryffindor
contadorR = 0  # Ravenclaw
contadorH = 0  # Hufflepuff
contadorS = 0  # Slytherin

# Pregunta 1
print("P1) Do you like Dawn or Dusk?")
print("1) Dawn") 
print("2) Dusk")

respuestaP1 = int(input("Enter your answer (1-2): "))

if respuestaP1 == 1:
    contadorG += 1
    contadorR += 1
elif respuestaP1 == 2:
    contadorH += 1
    contadorS += 1
else:
    print("Please, answer 1-2")

# Pregunta 2
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good") 
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

respuestaP2 = int(input("Enter your answer (1-4): "))

if respuestaP2 == 1:
    contadorH += 2
elif respuestaP2 == 2:
    contadorS += 2
elif respuestaP2 == 3:
    contadorR += 2
elif respuestaP2 == 4:
    contadorG += 2
else:
    print("Please, answer 1-4")

# Pregunta 3
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin") 
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

respuestaP3 = int(input("Enter your answer (1-4): "))

if respuestaP3 == 1:
    contadorS += 4
elif respuestaP3 == 2:
    contadorH += 4
elif respuestaP3 == 3:
    contadorR += 4
elif respuestaP3 == 4:
    contadorG += 4
else:
    print("Please, answer 1-4")

# Determinar la casa según los contadores
if contadorS > contadorG and contadorS > contadorH and contadorS > contadorR:
    print("Tu casa es Slytherin!")
elif contadorG > contadorS and contadorG > contadorH and contadorG > contadorR:
    print("Tu casa es Gryffindor!")
elif contadorH > contadorG and contadorH > contadorS and contadorH > contadorR:
    print("Tu casa es Hufflepuff!")
else:
    print("Tu casa es Ravenclaw!")
