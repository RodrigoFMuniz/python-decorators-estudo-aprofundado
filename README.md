# Decorators

- São ferramentas para facilitação do uso de **closures**
- Closures são um caso especial de **aninhamento de funções** de **ordem superior**, que armazenam **variáveis livres**
- Funções aninhadas são funções definidas dentro de funções
- Funções de ordem superior são funções que podem receber, ou retornar funções de **primeira classe**
- Funções de primeira classe são funções como objetos. Elas podem ser colocadas em variáveis, colocadas em containeres e,passadas/retornadas por funções.
- Variáveis livres não pertecem nem ao escopo local, nem ao global.

## Funções como objetos

- Em python, funções são objetos.
- Isso significa que podemos atribuir funções a variáveis e colocá-las em containeres.
- Exemplo

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
