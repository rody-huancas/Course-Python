"""
Ejercicio 04: Conversor de Monedad
Crear un sistema que convierta de moneda nacional a dólares por ejemplo de soles peruanos a dólares, pesos mexicanos a dólares, pesos colombianos a dólares.

Para solucionar este problema se requiere que el usuario ingrese la cantidad de monedas nacionales y luego realizar la conversión.

Para este sistema debe hacer un menú de navegación para seleccionar a que tipo de moneda se ara la conversión y también para cerrar el programa, el sistema no se debe cerrarse si no lo deseas.
"""


def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f'Ingrese la cantidad de {pais}: '))
    dolares = cantidad_moneda / valor_dolar
    # redondear a 2 decimales
    dolares = round(dolares, 2)
    print(f'Tienes ${dolares} Dolares')


def main():
    while True:
        menu = """
        1. Soles Peruanos a Dolares
        2. Pesos Mexicanos a Dolares
        3. Pesos Colombianos a Dolares
        4. Salir

        Ingrese una opción: 
        """
        opcion = input(menu)
        if opcion == '1':
            convertir(3.61, 'Soles Peruanos')
        elif opcion == '2':
            convertir(20, 'Pesos Mexicanos')
        elif opcion == '3':
            convertir(3471.27, 'Pesos Colombianos')
        elif opcion == '4':
            print("Cerrando conversor de monedas")
            break
        else:
            print('Opción incorrecta, ingrese una opción correcta')


if __name__ == '__main__':
    main()
