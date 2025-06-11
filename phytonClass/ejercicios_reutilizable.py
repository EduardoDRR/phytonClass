# diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
# edad_minima = min(diccionario_edades.values())
# ultimo_nombre = max(diccionario_edades.keys())
# print(edad_minima)      # Imprime 2
# print(ultimo_nombre)    # Imprime Sebastián
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [round((f - 32) * 5/9, 2) for f in temperatura_fahrenheit]
print(grados_celsius)  # Imprime [0.0, 100.0, 135.0]