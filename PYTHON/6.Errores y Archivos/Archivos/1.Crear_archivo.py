from io import open
from os import path


def escribir_archivo():
    # Escribir en el archivo, si el archivo no existe, lo crea automaticamente
    archivo = open('texto.txt', 'w')
    # Escribir en el archivo
    archivo.write('Hola Mundo')
    # Cerrar archivo
    archivo.close()

# escribir_archivo()


# Leer Archivo
def leer_archivo():
    # Si existe el archivo
    if path.isfile('texto.txt'): 
        archivo = open('texto.txt', 'r')
        # textos = archivo.read()
        # leer el archivo y agregarlo a una lista cada linea
        textos = archivo.readlines()
        archivo.close()
        print(textos)
    else: print('No existe el archivo')

# leer_archivo()


# Agregar datos al archivo
def agregar_datos():
    if path.isfile('texto.txt'): 
        archivo = open('texto.txt', 'a')
        # Escribir en una nueva línea
        archivo.write('\nHola Rody')
        archivo.close()
    else: print('No existe el archivo')

# agregar_datos()


# Modificar los datos del archivo
def modificar_datos():
    if path.isfile('texto.txt'): 
        archivo = open('texto.txt', 'r+')
        texto = archivo.readlines()
        print(texto)
        texto[1] = "Hola Dev\n"
        archivo.write('\nHola Pedro')
        print(texto)
        # colocar el puntero al inicio
        archivo.seek(0)
        # reescribir
        archivo.writelines(texto)
        archivo.close()
        print(texto)
    else: print('No existe el archivo')

# modificar_datos()


# Eliminar datos
def eliminar_datos():
    archivo = open('texto.txt', 'w')
    archivo.close()

# eliminar_datos()

