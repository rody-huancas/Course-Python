# METODOS PARA CADENAS

mensaje = 'Hola Mundo'

# Convertir una cadena a mayúsculas
print(mensaje.upper())

# Convertir a minúsculas
print(mensaje.lower())

mensaje2 = 'saludos desde la tierra'

# Convertir la primera letra mayúscula
print(mensaje2.capitalize())

# Convertir la primera letra de cada palabra a mayúsculas
print(mensaje2.title())

# Contar cuantas letras hay en una cadena
print(mensaje2.count('a'))


# eliminar los espacios en blanco al inicio y al final
print('     Rody Huancas     '.strip())


# eliminar los caracteres que se indiquen, en este caso eliminará los caracteres al inicio y al final
print('-----Rody - Huancas-----'.strip('-'))

# Convertir una cadena a una lista
# Convierte cada palabra en elemento de una lista
print('Hola Mundo Desde La Tierra'.split())
