import collections
import random

def criptograma(jugador):
    print('Criptograma')
    print('----------------------')
    print('Pierde una vida por partida perdida')
    print('----------------------')


    a= [2,4,5]
    n = random.choice(a)
    #numero de saltos
    abecedario = collections.deque(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

    print(list(abecedario))
    abecedario.rotate(n)
    abecedario_shift_2_espacios = list(abecedario)
    print(abecedario_shift_2_espacios) 


    mensaje="si te graduas pisas el saman"
    letras=list(mensaje)
    #print(mensaje)
    frase=''

    for i in range(len(letras)):
        Valor_num=ord(letras[i])+n
        
        if Valor_num>122 or (Valor_num>90 and Valor_num<97):
            Valor_num-=26
        if letras[i]!=' ':
            letras[i]=chr(Valor_num)
    #for i in range(len(letras))
    #    frase

    frase="".join(map(str, letras))
    print(frase)

    respuesta = ''
    while respuesta != mensaje:
        respuesta = input('Ingrese el mensaje codificado: \n').lower()
        if respuesta.lower() == mensaje.lower():
            print('Correcto')
            
        elif respuesta != mensaje:
            print('Incorrecto')
            jugador.vida=-1/2
        
        
