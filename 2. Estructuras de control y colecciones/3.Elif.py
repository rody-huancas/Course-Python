# ELIF

# Comprobar
v = input("Ingrese un caracter: ")

# Si v es igual a "a" o es igual a "A"
if v == "a" or v == "A":
    print(f"vocal {v}")
elif v == "e" or v == "E":
    print(f"vocal {v}")
elif v == "i" or v == "I":
    print(f"vocal {v}")
elif v == "o" or v == "O":
    print(f"vocal {v}")
elif v == "u" or v == "U":
    print(f"vocal {v}")
# Si ninguna de las codiciones anteriores se cumplió
else:
    print(f"La letra {v} no es vocal")
