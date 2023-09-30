import random
def ahorcado():
    
    print("Ahorcado")
    print("------------------------")
    print("Pierdes un cuarto de vida por letra incorrecta")
    print("------------------------")
    lista_palabras = ['metromix','rectorado','piscina']
    lista_preguntas=['me encuentro en la entrada de la universidad','tienes que subir muchos pisos para llegar a mi','me buscan y nunca me encuentran en la universidad']
    num = random.randint(0,2)
    palabra = lista_palabras[num]
    print(lista_preguntas[num])
    intentos = 7
    entrada = ''
    entrada_valida = set('abcdefghijklmnopqrstuvwxyz')

    while len(palabra)>0:
        palabra_1 = ""


        for letra in palabra:
            if letra in entrada:
                palabra_1 = palabra_1+letra
            else:
                palabra_1=palabra_1+"_ "

        if palabra_1 == palabra:
            print(palabra_1)
            print('Ganaste')
            break

        print('adivina las palabras',palabra_1)
        guess = input()

        if guess in entrada_valida:
            entrada = entrada+guess
        else:
            print('entra un caracter valido')
            guess=input()
        
        if guess not in palabra:
            intentos = intentos-1

            if intentos==6:
                print("Quedan 6 intentos")
                print("-----------------")
            elif intentos==5:
                print("Quedan 5 intentos")
                print("-----------------")
                print("       O        ")
            elif intentos==4:
                print("Quedan 4 intentos")
                print("-----------------")
                print("        O         ")
                print("        |         ")
            elif intentos==3:
                print("Quedan 3 intentos")
                print("-----------------")
                print("        O         ")
                print("        |         ")
                print("       /          ")
            elif intentos==2:
                print("Quedan 2 intentos")
                print("-----------------")
                print("        O         ")
                print("        |         ")
                print("       / \        ")

            elif intentos==1:
                print("Queda 1 intento")
                print("-----------------")
                print("        O/        ")
                print("        |         ")
                print("       / \         ")
            elif intentos==0:
                print("Perdiste")
                print("-----------------")
                print("       \O/         ")
                print("        |         ")
                print("       / \         ")        
