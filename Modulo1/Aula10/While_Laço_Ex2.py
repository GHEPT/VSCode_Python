#02 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexbio = input('Digite o seu sexo biológico [M/F]: ').strip().upper()
if sexbio == 'M':
    print('M - Masculino')
elif sexbio == 'F':
    print('F - Feminino')
else:
    while sexbio not in 'MF':
        while True:
            sexbio = input('Digite o seu sexo biológico [M/F]: ').strip().upper()
            if sexbio in 'MF':
                break
    if sexbio == 'M':
        print('M - Masculino')
    elif sexbio == 'F':
        print('F - Feminino')
