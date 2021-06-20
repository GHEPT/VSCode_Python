""" 
from time import sleep

for cont in range(10, 0, -1):
    print(cont, end =' ')
    sleep(1)
print('\nFeliz ano novo!')



cont = 10

while cont != 0:
    print(cont, end = ' ')
    sleep(1)
    cont -= 1
print('Feliz ano novo!') """

# for c in range(1, 4):
#     n = int(input('Digite um número: '))
#     print('Fim')

# n = 1
# while n != 0:
#     n = int(input('Digite um número: '))
# print('Fim')


# n = 1
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = input('Quer continuar? [S/N] ').upper()
# print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} números pares e {impar} números ímpares')
