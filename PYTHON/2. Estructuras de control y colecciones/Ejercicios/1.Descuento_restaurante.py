"""
Un restaurante ofrece un descuento del 10% para consumos de hasta a s/. 100, y 
un descuento del 20% para consumos mayores, para ambos casos se aplica un descuento
del 19%. Determinar el monto del descuento, el impuesto y el importe a pagar.

Para la solución, se requiere que el usuario ingrese el consumo y el sistema verifica
y calcula el monto del descuento, el impuesto y el importe a pagar
"""

# Entrada
consumo = float(input("Ingrese el consumo: "))

# Proceso
if consumo <= 100:
    # Descuento de 10%
    dato_descuento = "10%"
    descuento = consumo * 0.10
elif consumo > 100:
    # Descuento de 20%
    dato_descuento = "20%"
    descuento = consumo * 0.20

monto_descuento = consumo - descuento
igv = monto_descuento * 0.19
total_pagar = monto_descuento + igv

# Salida de datos
print("="*30)
print("===== FACTURA DE CONSUMO =====")
print(f"Descuento que se aplica {dato_descuento}")
print("="*30)
print(f"Consumo: {consumo}")
print(f"Descuento: {descuento}")
print(f"Monto con Descuento: {monto_descuento}")
print(f"IGV: {igv}")
print(f"Total a pagar: {total_pagar}")
print("="*30)
