# 03
# Desenvolva um código que pergunte um númeron para o usuário e exiba todos seus divisores.

n = int(input('Digite um número aleatório: '))

for c in range(1, n+1):
    if n % c == 0:
        print(f'{n} é divisível por {c} e o resultado é {n / c:.0f}')
