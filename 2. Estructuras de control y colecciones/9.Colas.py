# COLAS => El primer elemento en entrar es el primero en salir

# libreria para crear colas
from collections import deque

# Crear una cola
cola = deque(["Rody", "Juan", "Joel"])

# Agregar un elemento a la cola
cola.append("Luis")

# Quitar el primer elemento de la izquierda, es decir, el primero en entrar
primero = cola.popleft()
print(primero)
