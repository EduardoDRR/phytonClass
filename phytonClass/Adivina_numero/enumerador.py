''' enumerador '''
#Acceder a los indices de los elemtos de una lista con los elementos que tenemos hasta ahora
lista = ['a', 'b', 'c', 'd']
indice = 0

for item in lista:
	print(indice, item)  # Imprime el índice y el elemento de la lista
	indice+=1

#Acceder a los indices de los elemtos de una lista con la funcion enumerate
lista = ['a', 'b', 'c', 'd']	
for indice, item in enumerate(lista):
	print(indice, item)  # Imprime el índice y el elemento de la lista

#Se piede acceder a los indices sin tener una lista
for indice, item in enumerate(range(30,45)):
	print(indice, item)  # Imprime el índice y el elemento de la lista

#Se pueden crear tuples con enumerate y crear una lista
tuple = list(enumerate(lista))
print(tuple)  # Imprime el índice y el elemento de la lista
