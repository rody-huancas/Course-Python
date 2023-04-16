# DICCIONARIOS => contiene clave y valor, son como los arrays asociativos

# Definir diccionario
# definimos su clave(indice) y su valor
numeros = {'uno': 1, 'dos': 2, 'tres': 3}

# acceder a elemento mendiante su clave
# print(numeros['dos'])

# Agregar un elemento
# numeros['cinco'] = 5
# print(numeros)

# Buscar un valor, solo se busca por su valor
# print(numeros.get('tres', 'No se encontró'))

# Mostrar todas las claves
# print(numeros.keys())

# Mostrar los valores
# print(numeros.values())

# Mostrar la clave y valor
# print(numeros.items())

# Eliminar un elemento por medio de la clave
# print(numeros.pop("tres", "No se encontró"))
# print(numeros)

# Iterar sobre nuestro diccionario

# muestra solo las claves
# for numero in numeros:
#     print(numero)

# iterar sobre los valores
# for numero in numeros.values():
#     print(numero)


# iterar y mostrar clave y valor
for clave, valor in numeros.items():
    print(f"{clave} - {valor}")
