''' Set y todas sus propiedades '''
#Los sets son estructuras de datos que no permiten elementos duplicados, es decir, no se pueden modificar una vez creadas
#Este es un ejemplo de una declaracion de un set
#Los set no son ordenados, es decir, no se pueden acceder a los elementos por su posicion
mi_set = {1, 2, 3, 4}
print(type(mi_set))
print(mi_set)
otro_set = [1.2,3]
print(otro_set)

#Se puede saber el largo de un set
print("largo:", len(mi_set))  # Salida: 4

#Saber si un valor se ecuemtra en el set
print(3 in mi_set)  # Salida: True

#Se pueden unir varios sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print('\n',"Union de varios set:", set3)  # Salida: {1, 2, 3, 4, 5}

''' Metodo para agregar elementos a un set '''
#El metodo add() permite agregar un elemento a un set
set1 = {1, 2, 3}
set1.add(4)
print('\n',"Agregar un elemento a un set:", set1)  # Salida: {1, 2, 3, 4}

'''metodo para eliminar elementos de un set'''
#El metodo remove() permite eliminar un elemento de un set
set1 = {1, 2, 3}
set1.remove(2)
print('\n',"Eliminar un elemento de un set:", set1)  # Salida: {1, 3}

'''El metodo discard() permite eliminar un elemento de un set, pero no genera un error si el elemento no existe'''
#El metodo discard() permite eliminar un elemento de un set
#Es similar al metodo remove(), pero no genera un error si el elemento no existe
set1 = {1, 2, 3}
set1.discard(2)
print('\n',"Eliminar un elemento de un set:", set1)  # Salida: {1, 3}
#El metodo discard() no genera un error si el elemento no existe
set1.discard(4)
print('\n',"Descartar un elemento de un set:", set1)  # Salida: {1, 3}
