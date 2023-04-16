# Crear una excepcion heredando de Exception
class OperadorExcepcion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def dividir(a, b):
    if b == 0: raise OperadorExcepcion('No se puede dividir por cero')
    else: return a / b

dividir(4, 0)