''' Diferencias entre = y == en Python '''
#El operador = se utiliza para asignar un valor a una variable, mientras que el operador == se utiliza para comparar dos valores y verificar si son iguales.
#Por ejemplo:
x = 5  # Asignación de valor 5 a la variable x
y = 5  # Asignación de valor 5 a la variable y
print(x == y)  # Comparación: True, porque x e y son iguales

''' Operadores logicos y sus usos '''
#Los operadores lógicos en Python son: and, or y not.
#Estos operadores se utilizan para combinar expresiones booleanas y evaluar condiciones complejas.
#Por ejemplo:
x = 5
y = 10
z = 15
print((x < y) and (y < z))  # True, porque ambas condiciones son verdaderas
print((x < y) or (y > z))  # True, porque al menos una condición es verdadera	
print(not (x < y))  # False, porque la condición es verdadera y el operador not la invierte

''' Operadores de comparación '''
#Los operadores de comparación en Python son: ==, !=, <, >, <= y >=.
#Estos operadores se utilizan para comparar valores y devolver un resultado booleano (True o False).
#Por ejemplo:
x = 5
y = 10
print(x == y)  # False, porque x e y no son iguales
print(x != y)  # True, porque x e y son diferentes
print(x < y)   # True, porque x es menor que y
print(x > y)   # False, porque x no es mayor que y
print(x <= y)  # True, porque x es menor o igual que y
print(x >= y)  # False, porque x no es mayor o igual que y

''' Operadores de identidad '''
#Los operadores de identidad en Python son: is y is not.
#Estos operadores se utilizan para verificar si dos variables apuntan al mismo objeto en memoria.
#Por ejemplo:
x = [1, 2, 3]
y = x  # y apunta al mismo objeto que x
z = [1, 2, 3]  # z es un nuevo objeto con el mismo contenido que x
# print(x is y)  # True, porque x e y apuntan al mismo objeto
# print(x is z)  # False, porque x y z son objetos diferentes en memoria
# print(x is not z)  # True, porque x y z son objetos diferentes en memoria
# print(x is not y)  # False, porque x e y apuntan al mismo objeto

''' Operadores de pertenencia '''
#Los operadores de pertenencia en Python son: in y not in.	
#Estos operadores se utilizan para verificar si un valor pertenece a una secuencia (como una lista, tupla o cadena).
#Por ejemplo:	
x = [1, 2, 3, 4, 5]
print(3 in x)  # True, porque 3 está en la lista x
# print(6 not in x)  # True, porque 6 no está en la lista x
# print(1 in x)  # True, porque 1 está en la lista x	
# print(7 not in x)  # True, porque 7 no está en la lista x
# print(2 in x)  # True, porque 2 está en la lista x
# print(8 not in x)  # True, porque 8 no está en la lista x

