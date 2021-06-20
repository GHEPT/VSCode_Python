#1.	Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números. {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  

""" num = dict()

num['1'] = 1
num['4'] = 16
num['5'] = 25
num['6'] = 36
num['7'] = 49
num['9'] = 81

print(num) """

# 2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado. {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 

""" num = dict()

for k in range(1, 10+1):
    num[k] = k ** 2
print(num) """

# 3.	Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

""" escola = dict()

escola['Nome'] = input('Digite o seu nome: ')
escola['Média'] = float(input('Digite sua média: '))
escola['Situação'] = ' '

if escola['Média'] > 7:
    escola['Situação'] = 'Você foi aprovado'
elif 5 <= escola['Média'] < 6.9:
    escola['Situação'] = 'Você está de recuperação'
elif escola['Média'] < 5:
        escola['Média'] = 'Você foi reprovado'

for i in escola:
    print()
print(escola) """


# 4.	Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.
""" 
from random import randint
from time import sleep
from operator import itemgetter


dados = dict()

for i in range(1, 4+1):
    dados[f'Jogador {i}'] = randint(1,6)

ranking = dict()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(ranking) """

# 5. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import date
cadastro = dict()

cadastro['Nome'] = input('Digite o seu nome: ')
ano = cadastro['Ano de Nascimento'] = int(input('Digite o ano de nascimento: '))
ctps = cadastro['CTPS'] = input('Informe o número da CTPS (digite 0 caso não tenha CTPS): ')
cadastro['Idade'] = date.today().year - ano
if ctps != 0:
    contr = cadastro['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['Ano da Aposentadoria'] = (contr - ano) + 35
    cadastro['Salário'] = float(input('Informe o salário em R$: '))

print(cadastro)
print(f'Você irá se aposentar com {cadastro["Ano da Aposentadoria"]} anos')