try:
    a = int(input('Ingrese el dividento: '))
    b = int(input('Ingrese el divisor: '))

    divi = a / b

except ValueError:
     print("Error, ingrese solo números enteros")
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except Exception as error:
    print(f'Ha ocurrido un error: {type(error).__name__}')
    

print(f'La division es: {divi}')