import random

def palabra_mezclada():

    def mezcla(cocina):
        cocina=list(cocina)
        random.shuffle(cocina)
        return ''.join(cocina)


    print("Palabra mezclada.")
    print("----------------------------------")
    print("Palabra incorrecta = pierdes media vida.")
    print("----------------------------------")


    lista_categoria=[['sarten', 'paleta', 'olla', 'vaso', 'hornilla'],['poceta', 'cepillo', 'afeitadora', 'regadera', 'grifo'],['zumba','salsa','flamengo','tango','perreo']]
    categorias = [0,1,2]
    categoria = random.choice(categorias)
    correcta = 0

    while lista_categoria[categoria]:
        resultado_1 = print([mezcla(palabra) for palabra in lista_categoria[categoria]])
        pregunta_1= input('Introduce la palabra: ').lower()
        pregunta_1=pregunta_1.replace('\n','')
        for i in range(len(lista_categoria[categoria])):
            if(pregunta_1==lista_categoria[categoria][i]):
                print('correcto')
                lista_categoria[categoria].remove(pregunta_1)
                break

