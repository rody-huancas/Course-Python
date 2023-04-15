import mi_paquete.aritmetica as a


def main():
    suma = a.sumar(4, 4, 5, 8, 7, 9)
    resta = a.restar(20, 13)
    potencia = a.potencia(3, 3)
    print(f'La suma es {suma}')
    print(f'La resta es {resta}')
    print(f'La potencia es {potencia}')


if __name__ == '__main__':
    main()
