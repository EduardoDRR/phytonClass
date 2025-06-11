''' rango '''
#El rango en Python se refiere a una secuencia de números enteros.
#La función range() se utiliza para generar una secuencia de números, que se puede usar en bucles for.
#La función range() toma uno, dos o tres argumentos:
#1. range(stop): Genera números desde 0 hasta stop-1.	
#2. range(start, stop): Genera números desde start hasta stop-1.
#3. range(start, stop, step): Genera números desde start hasta stop-1, incrementando de step en step.	}

#Ejemplo de uso de range():
for i in range(5):
	print(i)  # Imprime los números del 0 al 4

#Ejemplo de uso de range() con start y stop:
for i in range(2, 6):
	print(i)  # Imprime los números del 2 al 5

#Ejemplo de uso de range() con start, stop y step:
for i in range(1, 10, 2):
	print(i)  # Imprime los números impares del 1 al 9

#Ejemplo de uso de range() con step negativo:
for i in range(10, 0, -2):
	print(i)  # Imprime los números pares del 10 al 2

#Tambien se puede usar range() para crear listas:
#Ejemplo de uso de range() para crear una lista:
lista = list(range(5))
print(lista)  # Imprime [0, 1, 2, 3, 4]