print ("Bienvenido maricon, que desea hacer?")
print ("selecciona 1 si quieres iniciar la partida")
print("1. Dific")
print 


eleccion = 0
dificultad = 0

while(eleccion<1) or (eleccion>3):
    
    eleccion = int(input())

    if eleccion == 1:
        while (dificultad<1) or (dificultad>3):
            dificultad = int(input("Seleccione dificultad: "))
            if dificultad == 1 :
                print("facil como tu")
            elif dificultad == 2 :
                print("Normal como tu")
            elif dificultad == 3 :
                print("Dificil no como tu perra te cague")
    elif eleccion == 2:
        print ("Instrucciones: ")
    elif eleccion == 3:
        print ("Estos son los records: ")
    else:
        print ("Pajuo, por favor ingrese un numero valido")