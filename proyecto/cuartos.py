from ahorcado import ahorcado
from criptograma import criptograma
from palabramezclada import palabra_mezclada
from unnumeroentre import numero_entre

def movimiento(derecha,izquierda):
    pregunta = input('A donde desea ir?')
    if pregunta == 'derecha'.lower():
        derecha()
    elif pregunta == 'izquierda'.lower():
        izquierda()



def biblioteca():
    print('Estas en la Biblioteca, A donde quieres ir?')
    respuesta = "no"
    while respuesta == "no":
        respuesta = input('Izquierda\nCentro\nDerecha \nO escribe "moverse" para cambiar de cuarto\nRespuesta: ').lower()
        respuesta=respuesta.replace("\n","")
        if respuesta == "Izquierda".lower():
            print('Estas en el mueble de sentarse')
            respuesta = input('Necesito que sepas derivar \nJugar:"Preguntas de matematica?\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                juegos_mate()
                
        elif respuesta == "Centro".lower():
            print('Estas frente un mueble de libros')
            respuesta = input('Deseas sacar un libro\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                ahorcado()
        
        elif respuesta == "Derecha".lower():
            print('Estas frente a un mueble con gabetas')
            respuesta = input('Yes\nNo\n').lower()
            if respuesta == 'Yes'.lower():
                criptograma()

        elif respuesta == 'Moverse':
            movimiento(puerta,saman)

biblioteca()


def saman():
    print('Estas en el Saman')
    respuesta = "No"
    while respuesta == "No":
        respuesta = input('A donde quieres ir\nIzquierda\nCentro\nDerecha \nO escribe "moverse" para cambiar de cuarto\nRespuesta: ').lower()
        
        if respuesta == "Izquierda".lower():
            print('Estas frente al primer Banco, deseas jugar al juego Quizziz')
            respuesta = input('Yes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                quizziz()

        elif respuesta == "Centro".lower():
            print('Estas al frente del Saman')
            respuesta = input('Deseas jugar el juego de logica?\nYes\nNo\nRespuesta: ')
            if respuesta == 'Yes'.lower():
                print('Encuentra la logica y resuelve')
                logica()
                

        elif respuesta == "Derecha":
            print('Estas al frente del Segundo Banco,desea jugar el juego de memoria')
            respuesta = input('Yes\nNo\Respuesta:').lower()
            if respuesta == 'Yes'.lower():
                memoria()

        elif respuesta == 'Moverse':
            movimiento(biblioteca,saman)
saman()






'''
def puerta():
    print('Estas frente a la puerta de los Laboratorios')
    respuesta = "No"
    while respuesta == "No":
        respuesta = input('A donde quieres ir \nCentro \nO escribe "moverse" para cambiar de cuarto\nRespuesta: ').lower()
        if respuesta == "Centro".lower():
            respuesta = input('Estas en el primer banco, quieres jugar el juego Quizziz?\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                quizziz()

        elif respuesta == "Centro":

        elif respuesta == "Derecha":

        elif respuesta == 'Moverse':
            movimiento(biblioteca,labs)
'''

def labs():
    print('Estas dentro de los Laboratorios')
    respuesta = "No"
    while respuesta == "No":
        respuesta = input('A donde quieres ir? \nIzquierda \nCentro \nDerecha \nO escribe "moverse" para cambiar de cuarto\nRespuesta: ').lower()
        if respuesta == "Izquierda".lower():
            respuesta = input('Estas frente a una computadora, desea jugar "Preguntas de Python"\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                preguntas_python()
        
        elif respuesta == "Centro".lower():
            respuesta = input('Te encuentras frente a la pizarra, desea jugar "Sopa de letras"\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                sopadeletras()
        
        elif respuesta == "Derecha".lower():
            respuesta = input('Estas frente la computadora, desea jugar "Adivinanzas"\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                adivinanzas()
        
        elif respuesta == "Moverse".lower():
            movimiento(puerta,servidores)


def servidores():
    print('Estas dentro del cuarto de servidores')
    respuesta = "No"
    while respuesta == "No":
        respuesta = input('A donde quieres ir? \nIzquierda \nCentro \nDerecha \nO escribe "moverse" para cambiar de cuarto\nRespuesta: ').lower()
        if respuesta == "Izquierda".lower():
            respuesta = input('Tienes el Rack de frente, desea jugar "palabra mezclada"\nYes\nNo\nRespuesta: ').lower()
            if respuesta == "Yes".lower():
                palabra_mezclada()
        
        elif respuesta == "Centro".lower():
            juego_libre()

        elif respuesta == "Derecha".lower():
            numero_entre()

        elif respuesta == "Moverse".lower():
            movimiento(servidores,labs)




