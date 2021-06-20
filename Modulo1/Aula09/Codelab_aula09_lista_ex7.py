# 7
# Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:

# “Telefonou para a vítima?”
# “Esteve no local do crime?”
# “Mora perto da vítima?”
# “Devia para a vítima?”
# “Já trabalhou com a vítima?”

# Se a pessoa responder positivamente a 2 questões:
# “Suspeita”
# Entre 3 e 4
# “Cúmplice”
# 5 “Assassino”
# Caso contrário, ele será classificado como “Inocente”.

a = input('Telefonou para a vítima? (sim ou não): ').strip().lower()
b = input('Esteve no local do crime? (sim ou não): ').strip().lower()
c = input('Mora perto da vítima? (sim ou não): ').strip().lower()
d = input('Devia para a vítima? (sim ou não): ').strip().lower()
e = input('Já trabalhou com a vítima? (sim ou não): ').strip().lower()

perg = [a, b, c, d, e]
resultado = 0

for i in perg:
    if i == 'sim':
        resultado += 1
if (resultado) == 2:
    print('Suspeito(a)')
elif (resultado) >= 3 and (resultado) <= 4:
    print('Cúmplice')
elif (resultado) == 5:
    print('Assassino(a)')
else:
    print('Inocente')
