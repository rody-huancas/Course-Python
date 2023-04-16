# OPERACIONES CON CADENAS

# Multiplicar cadenas
texto = "hola"
print(texto*3)  # multiplicará la cadena por 3, es decir, se repetirá 3 veces

# Suma 2 cadenas
texto1 = "Hola"
texto2 = "Mundo"
print(texto1+texto2)

# Multiplicar una cadena y luego sumarla
texto3 = "Python"
texto4 = "Desde cero"

print((texto3 * 3)+texto4)

# Acceder a un caracter de una cadena
texto5 = "PYTHON"
print(texto5[1])  # acceder a la letra "Y"

# Obtener los caracteres desde un punto de inicio, hasta un punto fin
# acceder a los caracteres desde la posición cero, hasta la posición 3
print(texto5[0:3])

# Obtener los caracteres desde el inicio al caracter 4
print(texto5[:4])

# Obtener los caracteres desde el punto 2 hasta el final
print(texto5[2:])

# Contar la catidad de caracter
print(len(texto5))
