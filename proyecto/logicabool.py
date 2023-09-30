import random

print('Logica Booleana')
print('------------------------')
print('Pierde media vida por opción incorrecta')
print('------------------------')

a,b = False, True 
out = (a and b and not a) or (not b) or (b and a) or (a and not a and not b)

c, d = False, True
out_1 = (c and d and c) or (d) or (d or c) or (c and not a and not d)

elecciones= [0,1]
eleccion = random.choice(elecciones)

if eleccion==0:
    texto ='a, b = False, True \nout = (a and b and not a) or (not b) or (b and a) or (a and not a and not b)'
    print(texto)
    r = input('Cual es el valor del out de la siguiente logica? \nRespuesta: ')
    if r == str(out).lower():
        print('Correcto')
    else:
        print("Incorrecto")


if eleccion==1:
    texto_1 = 'a, b = False, True, out = (a and b and a) or (b) or (b or a) or (a and not a and not b)'
    f = input('Cual es el valor del out de la siguiente logica? \nRespuesta: ')
    if f == str(out_1).lower():
        print('Correcto')
    else:
        print('Incorrecto')