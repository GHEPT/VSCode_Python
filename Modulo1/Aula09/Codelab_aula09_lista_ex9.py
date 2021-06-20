# 9
# Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.

# Dados:
# Cada palpite possui 6 dezenas
# As dezenas variam de 1 até 60
# Não pode repetir dezena

total = 0
for dez1 in range(60):
    for dez2 in range(dez1 + 1, 60):
        for dez3 in range(dez2 + 1, 60):
            for dez4 in range(dez3 + 1, 60):
                for dez5 in range(dez4 +1, 60):
                    for dez6 in range(dez5 + 1, 60):
                        total += 1
print(total)
