"""
Ejercicio 01: Palíndromo
Crear un sistema que detecte si una palabra es palíndroma o no

Para solucionar este problema el usuario tiene que ingresar por pantalla una palabra y el sistema verificas si es palíndromo o no.

Una palabra palíndroma se lee de igual formo como de la derecha y de la izquierda.
"""

# definir función para verificar si es palíndromo


def palindromo(palabra):
    # Reemplazar los espacios en blanco
    palabra = palabra.replace(' ', '')
    # convertir a minúscula
    palabra = palabra.lower()
    # invertir palabra
    palabra_invertida = palabra[::-1]
    # Si la palabra es igual a la palabra invertida
    if palabra == palabra_invertida:
        return True
    else:
        return False


# Función principal
def main():
    palabra = input("Ingrese una palabra: ")
    # guardar el resultado de la funcion palindromo en la variable es_palindromo
    es_palindromo = palindromo(palabra)
    # Si es palindromo
    if es_palindromo:
        print(f'La palabra {palabra} es palindromo')
    # Si no es palindromo
    else:
        print(f'La palabra {palabra} NO es palindromo')


# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()
