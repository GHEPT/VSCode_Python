#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data = input('Digite uma data no formato XX/XX/XXXX: ')
dia = data[0:2] # VARIÁVEL PARA USAR NA F STRING
mes = int(data[3:5]) # VARIÁVEL TRANSFORMADA EM Nº INTEIRO PARA CONSULTAR ÍNDICE NA LISTA E USAR NA F STRING
ano = data[6:10] #VARIÁVEL PARA USAR NA F STRING
print('-=' * 40)
print(f'{dia} de {meses[mes - 1]} de {ano}')
print('-=' * 40)
