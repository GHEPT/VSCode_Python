#01 - Escreva um programa que pede a senha ao usuário e só sai do looping quando digitarem corretamente a senha.

senha = '#BoraCodar2021'

a = input('Digite a sua senha: ')
if a != senha:
    while True:
        a = input('Senha incorreta.\nDigite a sua senha: ')
        if a == senha:
            break
print('Bem vindo, Eduardo!')
