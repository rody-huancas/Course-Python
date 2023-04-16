# FOR LOO

# lista de datos
datos = ["Rody", "Juan", "Luis", "Pedro"]

# Iterar datos con la variable dato
for dato in datos:
    print(dato)


# También se puede hacer con un WHILE
c = 0
while c < len(datos):
    print(datos[c])
    c += 1

# Mostrar un listado de numeros con for
# mostrar los números en un rango de 0 a 9, tambien se puede agregar otro valor: range(10, 20)=> mostrará una lista de numeros desde 10 hasta 20
for n in range(10):
    print(n)
