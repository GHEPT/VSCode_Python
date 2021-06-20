#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

# INPUTS DO USUÁRIO SEM ESPAÇOS NAS EXTREMIDADES, TODAS MINÚSCULAS E CONSIDERANDO SOMENTE O PRIMEIRO CARACTERE
a = input('Telefonou para a vítima? (sim ou não): ').strip().lower()[0]
b = input('Esteve no local do crime? (sim ou não): ').strip().lower()[0]
c = input('Mora perto da vítima? (sim ou não): ').strip().lower()[0]
d = input('Devia para a vítima? (sim ou não): ').strip().lower()[0]
e = input('Já trabalhou com a vítima? (sim ou não): ').strip().lower()[0]

perg = [a, b, c, d, e] # LISTA PARA USAR NO CONTADOR
resultado = 0 # VARIÁVEL QUE VAI RECEBER A QUANTIDADE DE RESPOSTAS POSITIVAS

for i in perg: # CONTADOR FAZ UMA PERGUNTA POR VEZ
    if i == 's': # CASO A RESPOSTA SEJA POSITIVA
        resultado += 1 # VARIÁVEL SOMA 1 
if resultado == 2: # TESTE LÓGICO PARA DAR O RESULTADO
    print('-=' * 30)
    print('Você é considerado(a) [ SUSPEITO(A) ]')
    print('-=' * 30)
elif resultado >= 3 and resultado <= 4:
    print('-=' * 30)
    print('Você é considerado(a) [ CÚMPLICE ]')
    print('-=' * 30)
elif resultado == 5:
    print('-=' * 30)
    print('Você é considerado(a) [ ASSASSINO(A) ]')
else:
    print('-=' * 30)
    print('Você é considerado(a) [ INOCENTE ]')
