# 6
# O Sr.Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de1,99.
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

import time

a = float(input('Informe o valor do pão: ').replace(',', '.'))
print(f'\nPreço do pão: R$ {a}')
print('Panificadora Pão de Ontem - Tabela de Preços\n')
print(f'1 pãozinho - R$ {1 * a:.2f}')
time.sleep(.3)
for i in range(2, 50+1):
    print(f'{i} pãezinhos - R$ {i * a:.2f}')
    time.sleep(.3)
