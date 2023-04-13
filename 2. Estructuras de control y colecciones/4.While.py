# BUCLE WHILE
"""
# Listar los número del 1 al 10
c = 1

# Mientras que "c" sea menor o igual a 10
while c <= 10:
    # Imprimir números
    print(f"Número: {c}")
    # Incrementar en 1
    c += 1
"""

# Sumar números
n = int(input("Ingrese un número: "))

# crear variables e inicalizar
suma = 0
menores_n = 0

# Mientras que menores_n sea menor o igual a n
while menores_n <= n:
    # sumará la variable suma + menores_n
    suma += menores_n
    # incrementar en 1 menores_n
    menores_n += 1

# Imprimir la respuesta
print(f"La suma de {n} es: {suma}")
