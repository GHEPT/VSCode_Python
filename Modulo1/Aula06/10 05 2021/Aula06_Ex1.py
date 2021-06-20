# 1.Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a, b, c):
    somar = a + b + c
    print(f'A soma de {a} + {b} + {c} é: {somar}')


a = float(input("Digite o valor 1: "))
b = float(input("Digite o valor 2: "))
c = float(input("Digite o valor 3: "))

soma(a, b, c)