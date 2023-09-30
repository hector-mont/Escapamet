import random
def play():
    hecho = []
    tablero = [[[' X','😀'],[' X','🙄'],[' X','🤮'],[' X','🥰']],[[' X','🤮'],[' X','😨'],[' X','🤓'],[' X','😷']],[[' X','😨'],[' X','🤓'],[' X','🥰'],[' X','😷']],[[' X','🤑'],[' X','🤑'],[' X','🙄'],[' X','😀']]]
    random.shuffle(tablero)
    mostrar_tablero(tablero)


def mostrar_tablero(tablero):
    print('')
    
    for fila in range(len(tablero)):
        for i in range(len(tablero)):
            print(tablero[fila][i][1],end="")
        print('\n')

play()