# FUNCIONES RECURSIVAS

# calcular factorial
def factorial(n):
    # print(f'Valor inicial => {n}')
    if n > 1:
        n = n * factorial(n - 1)
    # print(f'Valor final => {n}')
    return n


# Ingresar el número manualmente
n = int(input('Ingrese un número: '))

# Guardar el resultado
resultado = factorial(n)
# Mostrar en consola
print(f'El facotorial de {n} es: {resultado}')
