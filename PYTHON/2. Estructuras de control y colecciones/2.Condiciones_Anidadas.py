# Condidciones anidadas

n = int(input("Ingrese un número entero: "))

# Si el número es diferente de cero
if n != 0:
    # si el número es mayo a cero
    if n > 0:
        # si la division del número entre 2 es igual a cero
        if n % 2 == 0:
            print(f"El número {n} es par")
        else:
            print(f"El número {n} es impar")
    else:
        # si la division del número entre 2 es igual a cero
        if n % 2 == 0:
            print(f"El número {n} es par negativo")
        else:
            print(f"El número {n} es impar negativo")
# Sino
else:
    print(f"El {n} es neutro")
