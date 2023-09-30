class Persona (): 
    tiempo = ' ' 
    username = ' '
    password = ' '
    edad = ' '
    vida = ' '
    dificultad = 0

i=0
jugadores=list()
archivo = open("registro.txt","r")
This_line=archivo.readline()
while This_line:
    jugador=Persona
    jugador.username = This_line
    This_line=archivo.readline()
    jugador.edad = This_line
    This_line=archivo.readline()
    jugador.vida = This_line
    This_line=archivo.readline()
    jugador.dificultad = This_line
    This_line=archivo.readline()
    jugador.username=jugador.username.replace("\n",'')

    jugadores.append(jugador)

    print("User: ",i+1,":",jugadores[i].username)
    print("Edad: ",jugadores[i].edad)
    print("Dificultad: ",jugadores[i].dificultad)
    print("Vidas: ",jugadores[i].vida)
    i+=1
    
i=0
user = input("dame tu user: ")
existe=0
for jugador_1 in jugadores:
    if user == jugadores[i].username:
        existe=1
        break
    i+=1





juan = Persona
juan.username = input("dame tu username: ")
juan.edad = input("Dame tu edad: ")
juan.password = input("Introduce tu contraseña: ")
x = input("Selecciona dificultad: \n1)Facil \n2)Normal \n3)Dificil \n")
if int(x)==1:
    juan.vida= 5
    juan.dificultad= 'Facil'
    print('tienes 5 vidas')
elif int(x)==2:
    juan.vida= 3
    juan.dificultad='Normal'
    print("tienes 3 vidas")
elif int(x)==3:
    juan.vida = 1
    juan.dificultad = 'Dificil'
    print("tienes 1 vida")
else:
    print('seleccione dificultad por favor')



archivo = open("registro.txt","a")
archivo.write(juan.username)
archivo.write("\n")
archivo.write(juan.edad)
archivo.write("\n")
archivo.write(str(juan.vida))
archivo.write("\n")
archivo.write(str(juan.dificultad))
archivo.write("\n")



archivo.close()








