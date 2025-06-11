'''Tuples y todas sus propriedades'''
#Las tuplas son estructuras de datos INMUTABLES, es decir, no se pueden modificar una vez creadas
#Este es un ejemplo de una declaracion de un tuple
mi_tupla = (1,2,3,4)
print(type(mi_tupla))

#Se pueden crear tuplas de cualquier tipo de dato
t = (1,2,3,4,5.0,"Hola",True)
print(t)
#Obviemanete se puede acceder a los elementos de la tupla
print(t[5]) #5

# Tuples pueden contener otros tuples, se pueden anidar
tupla_anidada = (1, (2, 3), 4)
print('\n',"Acceder a la tupla anidada y sus elementos:")
print( tupla_anidada[1])  # Salida: (2, 3)
print(tupla_anidada[1][0]) # Salida: 2

#Se pueden desempaquetar los elementos de una tupla, siempre y cuando el numero de variables coincida con el numero de elementos de la tupla
tupla = (1, 2, 3)
a, b, c = tupla
print('\n',"Desempaquetado:", a, b, c)  # Salida: 1 2 3

#podemos saber las veces quese repite un elemento en la tupla
tupla = (1, 2, 3, 1, 4, 5, 1)
print('\n',"Contar el elemento 1 en la tupla:", tupla.count(1))  # Salida: 3

#cambiar el tipo de dato de una tupla a lista
mi_lista = list(tupla)