def soma(a, b):
    return a+b


def sub(a, b):
    return a-b


def calculadora(op, x, y):
    operacoes = {
        '+': soma,
        '-': sub
    }
    return operacoes[op](x, y)


print(calculadora('-', 5, 6))
