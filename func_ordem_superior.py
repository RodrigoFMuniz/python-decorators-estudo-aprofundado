from functools import reduce


def soma(a, b):
    return a+b


resultado = reduce(soma, [1, 2, 3, 4, 5])

print(resultado)
