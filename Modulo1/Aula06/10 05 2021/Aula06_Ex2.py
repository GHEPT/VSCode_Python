# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def pos_neg(num):
    if num > 0:
        print('P')
    elif num < 0:
        print('N')
    else:
        print('0')


num = float(input('Digite um valor: '))
pos_neg(num)
