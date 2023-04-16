# Crear una clase

class Persona:
    # Definir atributos
    # nombre = None
    # edad = None

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # definir métodos
    def mostrar_datos(self):
        print(f'Su nombre es: {self.nombre}')
        print(f'Su edad es: {self.edad}')

    # Mostrar el estado del objeto 
    def __str__(self):
        return f'Su nombre es: {self.nombre} y su edad es: {self.edad}'