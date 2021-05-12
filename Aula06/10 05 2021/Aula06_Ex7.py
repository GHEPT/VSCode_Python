# funcao recebe 2 valores, imprime o menor e se forem iguais passa essa informacao

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