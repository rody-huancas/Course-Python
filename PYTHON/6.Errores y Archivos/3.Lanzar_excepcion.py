# LANZAR EXCEPCIONES

def dividir(a, b):
    if b==0: raise ZeroDivisionError('ERROR!, no se puede dividir entre cero.')
    else: return a / b

dividir(1,0)