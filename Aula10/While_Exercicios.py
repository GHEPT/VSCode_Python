""" 
n = input('Digite o seu nome: ')
s = input('Insira a sua senha: ')
t = 'Senha incorreta. Tente novamente.\n'
l = [n, s, t]

senha = 'aula10'

while s != senha:
    print(t)
    s = input('Insira sua senha: ')
print(f'\nBem vindo, {n}')



 """

 # Ex: 02

# a = input('Insira o seu sexo biológico [M/F]: ').upper()
# while a != 'M' and a != 'F':
#     a = input('Insira o seu sexo biológico [M/F]: ').upper()
# print('Obrigado')


# EX 03:

from random import randint

r = randint(0, 10+1)
n = int(input('Digite um número inteiro entre 0 e 10: '))
l = list()

while r != n:
    l.append(1)
    tam = len(l)
    n = int(input('Digite um número inteiro entre 0 e 10: '))

print(f'\nVocê acertou com {tam} palpite(s)!')
