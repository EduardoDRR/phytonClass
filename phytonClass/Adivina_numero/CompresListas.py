'''El uso de listas por comprensión'''

palabra = "Python"
lista = []

for letra in palabra:
	lista.append(letra)
print(lista)

# Usando listas por comprensión
lista_comprension = [letra for letra in "Python"]
print(lista_comprension)	

# Usando listas por comprensión con numeros
numeros = [numero for numero in range(0, 21,2)]	
print(numeros)

# Usando listas por comprensión con condiciones
lista_condicion = [numero for numero in range(0,21,2) if numero * 2 > 10]
print(lista_condicion)

# Usando listas por comprensión con condiciones y else
lista_condicion_else = [numero if numero * 2 > 10 else "no" for numero in range(0,21,2)]
print(lista_condicion_else)

#Ejemplo de listas por comprensión con caso de uso de la lista de pies a Metros
pies = [10,20,30,40,50]
metros = [p/3.281 for p in pies]
print(metros)