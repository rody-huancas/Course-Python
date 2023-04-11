"""
Calcular el precio de venta
Enunciado: Dado el valor de venta de productos, hallar el IGV (18%)
y el precio de venta

Para la solución de este problema se requiere que el usuario ingrese el valor
de la venta del producto y el sistema realice el cálculo respectivo para hallar
el IGV y el precio de venta, para ello usar la siguiente expresion:

igv = vv * 0.18
pv = vv * igv
"""

print("================================")
print("       REALIZAR UNA VENTA       ")
print("================================")

# Entrada de datos
vv = float(input("Ingrese el valor de la venta: "))

# Operaciones
igv = vv * 0.18
pv = vv + igv

# Salida de datos
print(f"El valor de la venta es: {pv}")
