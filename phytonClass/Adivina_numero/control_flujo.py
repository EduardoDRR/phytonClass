'''Control de flujo en Python'''
#El control de flujo en Python se refiere a la forma en que se ejecutan las instrucciones en un programa.
#Esto incluye estructuras de control como condicionales (if, elif, else) y bucles (for, while).
#Estas estructuras permiten tomar decisiones y repetir acciones en función de ciertas condiciones.

#Ejemplo con condicionales:
x = 10
y = 20
if x < y:
	print("x es menor que y")
elif x > y:
	print("x es mayor que y")
else:
	print("x es igual a y")

#Ejemplo con bucles:
for i in range(5):
	print(i)  # Imprime los números del 0 al 4

#while i < 5:	
	print(i)  # Imprime los números del 0 al 4
	i += 1

#Ejemplo con break,pass continue:
	# break: Detiene un bucle antes de que termine.
	# continue: Salta a la siguiente iteración del bucle.
	# pass: No hace nada; se usa como marcador de posición.
for i in range(5):
    if i == 3:
        break  # Detiene el bucle cuando i es 3
    print(i)  # Salida: 0, 1, 2

for i in range(5):
    if i == 3:
        continue  # Salta la iteración cuando i es 3
    print(i)  # Salida: 0, 1, 2, 4
