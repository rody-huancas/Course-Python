# EXCEPCIONES

c = 0
suma = 0

while c < 3:
    try:
        n=int(input('Ingrese un número: '))
        suma += n
        c+=1
    except: 
        print('ERROR! Solo se aceptan números enteros')

print(f'La suma es {suma}')