# Exercício Treino 1

# Escreva uma função que recebe dois parâmetros(números) e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênticos.

def numeros(a, b):
    if a < b:
        print(a)
    elif a > b:
        print(b)
    else:
        print(f'Os valores são iguais')


a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))

numeros(a, b)
