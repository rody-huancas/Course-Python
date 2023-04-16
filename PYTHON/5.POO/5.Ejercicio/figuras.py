"""
Crear un módulo figuras.py, y dentro crea clases como Figura, Rectangulo, Circulo y la función probar_figura.
Crear una clase Figura, con atributo nombre. Crear también el constructor de la clase y los métodos necesarios área y el perímetro con instrucción pass.
Crear otra clase Rectángulo que herede de la clase Figura, con atributos base y altura. Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área y el perímetro.
Crear otra clase Circulo que herede de la clase Figura, con atributo radio. Crear también el constructor de la clase y reescribe los métodos de la clase Figura para calcular el área y el perímetro.
Crear una función probar_figura donde reciba un objeto para probar diferentes figuras como rectángulo o circulo. Y imprima el estado del objeto y como también el área y perímetro.
Crear un módulo principal main.py, luego importa desde el modulo figuras las clases Rectángulo, Circulo y la función probar_figura.
Crear la función principal que puede ser main() y el punto de entrada de la aplicación de Python y llama a ejecutar la función main().
Dentro de la función main() crea un sistema que tenga un bucle infinito y también tenga un menú de navegación donde las opciones sean 1-Rectangurlo 2-Circulo 4-Salir
En la opción 1 pide al usuario que ingrese base y altura del rectángulo y crea un objeto de rectángulo y ese objeto envía al funcion probar_figura()
En la opción 2 pide al usuario que ingrese el radio del circulo y crea un objeto de circulo y ese objeto envía al función probar_figura()
En la opción 3 termina el bucle infinito y se cierra el programa.
"""

import math

class Figura(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.nombre = __class__.__name__ #obtener el nombre
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def altura(self):
        return 2 * self.base + 2 * self.altura

    def perimetro(self):
        return 2 * self.base + 2 * self.altura

    def __str__(self):
        return f'{self.nombre} [base: {self.base} - altura: {self.altura}]'



class Circulo(Figura):
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f'{self.nombre} [radio: {self.radio}]'
        


def probar_figura(figura):
    print(figura)
    print(f'Area: {figura.area()}')
    print(f'Perimetro: {figura.perimetro()}')