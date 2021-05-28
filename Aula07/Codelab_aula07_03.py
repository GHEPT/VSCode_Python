# Exercício  Treino  3

# Crie  uma  função  que  receba  uma  string  como  argumento  e  retorne  a mesma  string  em  letras  maiúsculas. Faça  uma  chamada  à  função,  passando  como  parâmetro uma string.

def aumenta(texto):
    texto = texto.upper()
    print(texto)


texto = input('Digite uma palavra: ')
aumenta(texto)
