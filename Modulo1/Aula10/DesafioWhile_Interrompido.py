# Exercício
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

""" 
se tiver mais de 18 pontua na A menos de 20 pontuar em duas condições: A e C  
se for M vai pontuar na B
se for F e menor de 20 vai pontuar na C  """


info1 = list()
info2 = list()
info3 = list()

a = int(input('\nDigite a sua idade [1 a 100]: '))
b = input('Digite o seu sexo [M ou F]: ').strip().lower()
if a > 18:
    info1.append(1)
if b == 'm':
    info2.append(1)
if a < 20 and b == 'f':
    info3.append(1)
c = input('Deseja cadastrar mais alguém? [S ou N]: ').strip().lower()
if c == 's':
    while True:
        a = int(input('\nDigite a sua idade [1 a 100]: '))
        b = input('Digite o seu sexo [M ou F]: ').strip().lower()
        if a > 18:
            info1.append(1)
        if b == 'm':
            info2.append(1)
        if a < 20 and b == 'f':
            info3.append(1)
        c = input('Deseja cadastrar mais alguém? [S ou N]: ').strip().lower()
        if c == 'n':
            break
print(f'\nQuantas pessoas tem mais de 18 anos?: {sum(info1):.0f}')
print(f'Quantos homens foram cadastrados?: {sum(info2):.0f}')
print(f'Quantas mulheres tem menos de 20 anos?: {sum(info3):.0f}')
