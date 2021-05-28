# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def compara(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("Os valores são iguais")

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

compara(a, b)
