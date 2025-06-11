''' Proyecto Analizador de Texto '''

#El proyecto consiste en crear un analizador de texto que primero le pida al usuario que ingrese un texto y luego le pida que ingrese 3 letras de su eleccion.
#El programa debe devolverla siguiente informacion:
#1. La cantidad de veces que aparece cada letra en el texto
#2. La cantidad de palabras que contiene el texto
#3. La priemra letra que aparece en el texto y la ultima letra que aparece en el texto
#4. Como se veria el texto con las palabra en orden inverso
#5. Si parace la palabra "Python" en el texto
#Texto El dia de hoy me siento muy ciontenti de poder estudiar y disfritar de mi curso de phyton

print("Bienvenido al analizador de texto")
texto = input("Ingrese el texto de su eleccion: ")
texto = texto.lower() #Convertimos el texto a minusculas para evitar problemas de mayusculas y minusculas
letras = []
letras.append(input("Ingrese la primera letra de su eleccion: "))
letras.append(input("Ingrese la segunda letra de su eleccion: "))
letras.append(input("Ingrese la tercera letra de su eleccion: "))

#1. La cantidad de veces que aparece cada letra en el texto

print("Cantidad de veces que aparece cada letra en el texto:")			
count1 = texto.count(letras[0])
count2 = texto.count(letras[1])
count3 = texto.count(letras[2])
print(f"La letra {letras[0]} aparece {count1} veces")
print(f"La letra {letras[1]} aparece {count2} veces")
print(f"La letra {letras[2]} aparece {count3} veces")

#2. La cantidad de palabras que contiene el texto
palabras = texto.split()	
print("Cantidad de palabras que contiene el texto:", len(palabras))

#3. La priemra letra que aparece en el texto y la ultima letra que aparece en el texto
primera_letra = texto[0]
ultima_letra = texto[-1]
print("La priemra letra que aparece en el texto:", primera_letra)
print("La ultima letra que aparece en el texto:", ultima_letra)

#4. Como se veria el texto con las palabra en orden inverso
texto_invertido = texto.split()[::-1]
print("Texttp invertido:", texto_invertido)

#5. Si parace la palabra "Python" en el texto
if "phyton" in texto:
	print("La palabra 'Phyton' aparece en el texto")
else :
	print("La palabra 'Phyton' no aparece en el texto")