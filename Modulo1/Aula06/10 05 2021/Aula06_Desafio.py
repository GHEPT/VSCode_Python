# DESAFIO-Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

extenso = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = input('Digite uma data aleatória no formato XX/XX/XXXX: ')

dia = int(data[0:2]) # Extrai a informação do dia digitado e transforma em um inteiro dentro de uma variável
mes = int(data[3:5]) # Extrai a informação do mês digitado e transforma em um inteiro dentro de uma variável
ano = int(data[6:10]) # Extrai a informação do ano digitado e transforma em um inteiro dentro de uma variável

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): # Condição True para ano bissexto 
    print(extenso[mes - 1])
else:
    if dia == 29:
        print(f'Essa data não é válida, pois {ano} não é um ano bissexto')
    else:
        print(extenso[mes - 1])
