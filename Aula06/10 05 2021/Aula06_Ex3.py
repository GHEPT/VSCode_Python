def soma_imposto():
    c = custo * ((taxa_imposto / 100)+1)
    return c


custo = float(input('Digite o custo do produto: R$ '))
taxa_imposto = float(input('Digite a taxa de imposto (%): '))

print(f'\nO custo inicial do produto é: R$ {custo:.2f}')
print(f'A taxa de imposto é: {taxa_imposto:.0f} %')
print(f'Custo final do produto: R$ {soma_imposto():.2f}\n')
