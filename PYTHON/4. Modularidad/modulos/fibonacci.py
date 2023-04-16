# Fibonacci

def fibo(num):
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b
    print("")


def fibo2(num):
    resultado = []
    a, b = 0, 1
    while a < num:
        resultado.append(a)
        a, b = b, a + b

    return resultado
