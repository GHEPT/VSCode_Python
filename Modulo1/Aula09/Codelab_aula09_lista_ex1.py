# 1
# Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

n = int(input('Qual tabuada você quer que eu resolva?: \n'))

for i in range(1, 10+1):
    print(f'{n} x {i} = {n*i}')
