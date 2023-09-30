import random


def numero_entre():

    numero = random.randint(1,15)
    respuesta = 0
    pista=0

    print('Escoge un numero entre')
    print('------------------------')
    print('Un cuarto de vida menos por 3 intentos fallidas')
    print('------------------------')

    while int(respuesta) != numero:
        respuesta= input('Ingrese el numero que piensa\nSi desea una pista escriba "clue":\n').lower()
        if respuesta=='clue'.lower():
            pista=1
            respuesta=0
            continue
        if pista:
            if numero < int(respuesta):
                if numero < int(respuesta)-5:
                    print('Esta mucho mas abajo')
                else:
                    print('Esta un poco mas abajo')
            else: 
                if numero < int(respuesta)+5:
                    print('Esta un poco mas arriba')
                else:
                    print('Esta mucho mas arriba')
        else:
            if int(respuesta) == numero:
                print('Correcto')
            elif int(respuesta) != numero:
                print('Incorrecto')

