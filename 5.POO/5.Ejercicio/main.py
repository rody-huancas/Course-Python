from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """
            Menú
        1. Rectangulo
        2. Circulo
        3. Salir
        
        Ingresa una Opción: """
        opcion = input(menu)
        
        if opcion == '1':
            base = float(input('Ingrese la base: '))
            altura = float(input('Altura: '))
            r = Rectangulo(base, altura)
            probar_figura(r)
        elif opcion == '2':
            radio = float(input('Ingrese el radio: '))
            c = Circulo(radio)
            probar_figura(c)
        elif opcion == '3':
            print('Cerrando el sistema')
            break
        else:
            print('Ingrese una opción correcta.')


if __name__ == '__main__':
    main()