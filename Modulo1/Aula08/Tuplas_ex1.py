# 01
# Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições. 
# Dica: utilizar a biblioteca random doPython.

import random

a = random.randrange(1,50)
b = random.randrange(1,50)
c = random.randrange(1,50)
d = random.randrange(1,50)
e = random.randrange(1,50)

tupla = (a, b, c, d, e)
print(f'Números aleatórios: {tupla}')
print(f'Menor número: {min(tupla)}')
print(f'Maior número: {max(tupla)}')
