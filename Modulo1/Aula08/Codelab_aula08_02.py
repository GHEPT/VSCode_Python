# 02
# Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece as vogais a,e,i,o,u.

s = 0
frase = input('Digite uma frase: ').upper()

for c in (frase):
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        c = + 1
        s += c
print(f'A soma das vogais é: {s}')
