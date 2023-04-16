# BREAK Y CONTINUE

c = 0

# Mientras c sea menor a 10
while c < 10:
    print(c)
    c += 1

    if c == 5:
        # print("Termina el bucle")
        # Finalizar la ejecución
        # break

        # Saltar la iteración
        print("Salta a siguiente iteración")
        continue
    # print("Después de continue")
else:
    print("Fin del bucle")
