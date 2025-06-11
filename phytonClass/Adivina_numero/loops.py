''' Loops '''
#Loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or to repeat a block of code multiple times.
# There are two types of loops in Python: for loops and while loops.
# The for loop is used to iterate over a sequence, while the while loop continues until a certain condition is met.
# Loops can also be controlled using break, continue, and pass statements.

# While loop
# Contar hasta 5
contador = 1
while contador <= 5:
    print(contador)  # Salida: 1, 2, 3, 4, 5
    contador += 1  # Incrementar el contador

# For loop
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)  # Salida: 1, 2, 3, 4, 5
# Iterar sobre un rango de números
for i in range(5):  # Itera desde 0 hasta 4
    print(i)  # Salida: 0, 1, 2, 3, 4