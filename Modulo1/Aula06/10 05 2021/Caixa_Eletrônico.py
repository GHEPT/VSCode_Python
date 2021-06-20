valor = int(input('Valor para sacar [10 - 600]: '))

# Simulando com 69
cem = valor // 100 # = 0
valor = valor - (cem*100) # 69 - 0 = 69 

cinquenta = valor // 50 # 69 // 50 = 1
valor -= (cinquenta*50) # 69 - 50 = 19

dez = valor // 10 # 19 // 10 = 1
valor -= (dez*10) # 19 - 10 = 9

cinco = valor // 5 # 9 // 5 = 1
valor = valor - (cinco*5) # 9 - 5 = 4

um = valor

print(f'Notas de R$ 100,00: {cem}')
print(f'Notas de R$  50,00: {cinquenta}')
print(f'Notas de R$  10,00: {dez}')
print(f'Notas de R$   5,00: {cinco}')
print(f'Notas de R$   1,00: {um}')