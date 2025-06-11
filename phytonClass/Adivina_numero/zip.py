''' zip '''	
#la funcion Zip() toma iterables (puede ser cero o más), y devuelve un iterador de tuplas, donde el i-ésimo elemento de cada iterable se agrupa en una tupla.
# Si los argumentos son de longitud diferente, el iterador se detiene cuando el iterable más corto se agota.		

nombres = ["Ana", "Juan", "Pedro", "María"]
edades = [25, 30, 22, 28]
ciudades = ["Madrid", "Barcelona", "Valencia", "Mexico"] 

# Uniendo listas con zip
combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
	print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

