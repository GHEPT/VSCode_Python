# 04
# Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

texto = input('Digite uma frase: ')
vogais = 'aeiou'
for c in vogais:
    texto = texto.replace(c,' ')
print(texto)
