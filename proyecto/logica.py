import random


pregunta_1 = ['🧡+🧡+🧡=45 \n 🍌+🍌+🧡=23 \n 🍌+⏰+⏰=10 \n ⏰+🍌+🍌x🧡=?'] 
pregunta_2 = ['🐧+🐧+🐧=27 \n 🐧+🐝+🐝=19 \n 🐝+🐦+🐦=13 \n 🐝x🐧-🐦=?']

n = [0,1]
r = random.choice(n)

respuesta_primera_logica = 165
respuesta_segunda_logica = 41

if r==0:
    print(pregunta_1)
    respuesta = int(input('Cual es la respuesta: '))
    if respuesta == respuesta_primera_logica:
        print('Correcto')
    else:
        print('Incorrecto')


if r==1:
    print(pregunta_2)
    respuesta = int(input('Cual es la respuesta: '))
    if respuesta == respuesta_segunda_logica:
        print('Correcto')
    else:
        print('Incorrecto')