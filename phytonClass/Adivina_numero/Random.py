''' El uso de random y sus priencipales funciones '''
#El randmom es un modulo que permite generar numeros aleatorios, se tiene que importar

from random import *

#Genera un numero aleatorio dentro de un rango
aleatorio = randint(1, 50) #Genera un numero aleatorio entre 1 y 10
print(aleatorio)

#Generar un numero aleatorio de punto flotante
aleatorio_flotante = round(uniform(1, 5),2) #Delimitamos los deciames
print(aleatorio_flotante)

#random genera un numero aleatorio entre 0 y 1
aleatorio_random = random() #Genera un numero aleatorio entre 0 y 1	
print(aleatorio_random)

#Elegir un elemento aleatorio de una lista
colores = ['rojo', 'verde', 'azul', 'amarillo']
random_color = choice(colores) #Elige un elemento aleatorio de la lista	
print(random_color)

#Uso del shuffle para mezclar una lista
numeros = list(range(2,50,5)) #Genera una lista de numeros del 2 al 50 con un salto de 5
shuffle(numeros) #Mezcla los elementos de la lista
print(numeros) 