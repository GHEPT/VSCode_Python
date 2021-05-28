# Desafio 1
# Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.
# Exemplo: 3025 = 55 e 55**2 é igual á 3025

for i in range(1000, 10000):
    a = ((i / 100) // 1)
    b = ((i / 100) % 1) * 100
    l_inicio = [a, b]
    c = a + b
    d = c**2
    if i == d:
        print(i)
