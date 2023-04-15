class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def detalle_persona(self):
        print(f'Nombre: {self.nombre} - Edad: {self.edad}')

    def __str__(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad}'


# Para heredar, agregamos de que clase heradaremos, pero lo colocamos entre parentesis
class Cliente(Persona):
    pass


# Clase empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # heredadr los valores de Persona
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def detalle_empleado(self):
        super().detalle_persona()
        print(f'Sueldo: {self.sueldo}')

    def __str__(self):
        return super().__str__() + f' - Sueldo: {self.sueldo}'

