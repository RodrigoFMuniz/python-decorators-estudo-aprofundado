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


# soma2_e_3 = soma(2,3) # ou
soma2_e_3 = calculadora('+', 2, 3)

list_funcs = [soma, sub]

print(soma2_e_3)
print(list_funcs[0](2, 3))
print(list_funcs[1](10, 3))
