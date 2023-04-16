# ARGUMENTOS INDETERMINADOS

# Pasamos un argumento con un "*" al inicio cuando no sabemos cuantos argumentos vamos a pasar
# Y para enviarle argumentos por nombre, se usa "**", y cuando mandamos a llamar nos muestra por clave y valor
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n

    return suma, kwargs


print(sumar(1, 2, 3, 4, 5, nombre="Rody", apellidos="Huancas"))
