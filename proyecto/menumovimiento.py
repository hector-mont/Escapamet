def movimiento(derecha,izquierda):
    pregunta = input('A donde desea ir?')
    if pregunta == 'derecha'.lower():
        derecha()
    elif pregunta == 'izquierda'.lower():
        izquierda()
