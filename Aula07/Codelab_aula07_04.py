# Exercício 4

# Crie um programa que tenha uma função chamada voto ()que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

from datetime import date

def voto(a):
    if a < 16:
        print('NEGADO')
    elif a >= 16 and a < 18:
        print('OPICIONAL')
    else:
        print('OBRIGATÓRIO')


b = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
a = b - nasc

voto(a)
