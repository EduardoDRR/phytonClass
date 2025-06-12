# La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir algo asi como 'Bueno, Juan, he pensado un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cual crees que es el numero'. Entonces, en cada intento el jugador dira un  numero y el programa puede responder cuatro cosas distintas: 
#  Si el numero que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un numero que no esta permitido. 
#  Si el numero que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un numero menor al numero secreto.  
#  Si el usuario eligio un numero mayor al numero secreto, tambien se lo hara saber de la misma manera.  
#  Y si el usuario acerto el numero secreto, se le va a informar que ha ganado y cuantos 
# intentos le ha tomado. 

from random import *

print("Ingresa tu nombre")
nombre = input()
print(f'Hola {nombre}, he prensado en un numero entre 1 y 100, y tienes solo 8 intentos para adivinar cual crees que es el numero')
rand = randint(1-100)

contador = 1
while contador <= 8:
    print(f"intento:{contador} Ingrese un numero")  
    intento = input()
    if intento == rand:
        print(f"felicidades adivinitaste, te tomo {intento}")
        break
    if intento < 1 or intento > 100:
        print("Eligiste  un numero no valido")
    elif intento < rand:
        print("Tu respuesta es incorrecta y has elejido un numeor menor al pensado")
    elif intento > rand:
        print("Tu respuesta es incorrecta y has elejido un numero mayor al pensado")
	
    contador += 1 
    