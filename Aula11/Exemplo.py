""" pessoa = list()
pessoa.append('Thiago')
pessoa.append(27)

povoado = list()
povoado.append(pessoa[:])

pessoa[0] = 'Maria'
pessoa[1] = 34

povoado.append(pessoa[:])


print(povoado) """

# EX em aula junto com o professor
""" 
galera = list()
dados = list()
total_maior = total_menor = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear() # Limpa lista e coloca de novo

for g in galera:
    if g[1] >= 18:
        print(f'{g[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{g[0]} é menor de idade')
        total_menor += 1

print(f'Temos {total_maior} maiores e {total_menor} menores de idade') """

# # Exercício em aula pós intervalo

# # Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser, pare o programa.

# # Mostre:
# # Quantas pessoas foram cadastradas
# # Mostre o maior peso
# # Mostre o menor peso

# """ galera = list()
# dados = list()
# todos = 0

# while True:
#     dados.append(str(input('Digite o seu nome: ')))
#     dados.append(int(input('Digite o seu peso: ')))
#     galera.append(dados[:])
#     todos += 1
#     dados.clear()
#     cont = str(input('Deseja continuar? [S/N]: ')).upper()
#     if cont == 'N':
#         break

# print(f'No total, {todos} pessoas foram cadastradas')
# print(f'O maior peso foi: {max(galera[1])} kg')
# print(f'O menor peso foi: {min(galera[1])} kg') """


# galera = list()
# dados = list()
# maior = menor = 0

# while True:
#     dados.append(str(input('Digite o seu nome: ')))
#     dados.append(float(input('Digite o seu peso: ').replace(',', '.')))
    
#     if len(galera) == 0:
#         maior = menor = dados[1]
#     else:
#         if dados[1] > maior:
#             maior = dados[1]
#         if dados[1] < menor:
#             menor = dados[1]
#     galera.append(dados[:])
#     dados.clear()

#     resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
#     if resp == 'N':
#         break

# print(f'No total, {len(galera)} pessoas foram cadastradas')
# print(f'O maior peso foi: {maior} kg')
# print(f'O menor peso foi: {menor} kg')


# Palpites da Mega Sena

from random import randint
quant = int(input('Quantos jogos você quer sortear?: '))
lista_temp = list()
jogos = list()

for c in range(1, quant+1):
    while True:
        num = randint(1, 60)
        if num not in lista_temp:
            lista_temp.append(num)
