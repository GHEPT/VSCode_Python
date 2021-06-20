# Exercício 5

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(a=0, b=0):
    print(f'O jogador {a} tem {b} gols marcados')


a = input('Nome do jogador: ')
b = (input('Gols marcados: '))

ficha(a, b)
