# 3
# Faça um programa que leia o estado civil de 15 pessoas (Solteiro/Casado) e mostre ao final a quantidade de pessoas de cada estado civil.

solteiro = []
casado = []

for i in range(1, 15+1):
    resp = input('Digite seu estado civil (Solteiro / Casado): ').strip().lower()
    if resp == 'solteiro':
        solteiro.append(1)
    elif resp == 'casado':
        casado.append(1)
    else:
        0

print(f'Total de solteiros: {sum(solteiro)}')
print(f'Total de casados: {sum(casado)}')
