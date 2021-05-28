### PROJETO: Gastos com viagem

# Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.

# Passagem
# Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que a passagem para:
# - São Paulo custa R$ 312,00;
# - Porto Alegre custa R$ 447,00;
# - Recife custa R$ 831,00;
# - Manaus custa R$ 986,00.

# Hospedagem
# Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

# Aluguel de Carro
# Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
# - Calcule o custo do aluguel do carro sendo que:
# - A cada dia o carro custa R$ 40,00;
# - Alugando 7 dias ou +: R$ 50,00 de desconto;
# - Alugando 3 dias ou +: R$ 20,00 de desconto;
# - Você pode receber apenas um desconto;
# - Retorne o custo.

# Cálculo Total
# - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
# - Reutilize as funções já criadas.
# - Exiba o total da viagem chamando apenas a nova função declarada!

# Gastos Extras
# Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem. Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.

def chama():
    custo_aviao(cidade)

def custo_aviao(cidade):
    global c_cidade
    sp = 312
    pa = 447
    rec = 831
    ma = 986
    if cidade == 'são paulo':
        print(f'\nVôo para São Paulo R$ {sp:.2f}')
        c_cidade = sp
        custo_hotel(noites)
    elif cidade == 'porto alegre':
        print(f'\nVôo para Porto Alegre R$ {pa:.2f}')
        c_cidade = pa
        custo_hotel(noites)
    elif cidade == 'recife':
        print(f'\nVôo para Recife R$ {rec:.2f}')
        c_cidade = rec
        custo_hotel(noites)
    elif cidade == 'manaus':
        print(f'\nVôo para Manaus R$ {ma:.2f}')
        c_cidade = ma
        custo_hotel(noites)


def custo_hotel(noites):
    global c_noites
    c_noites = noites * 140
    print(f'Hotel para {noites} noites: R$ {c_noites:.2f}')
    custo_carro(dias)


def custo_carro(dias):
    global c_dias
    global gastos_extras
    if dias == 1:
        c_dias = 40
    elif dias >= 3 and dias <= 6:
        c_dias = (dias * 40) - 20
    else:
        c_dias = (dias * 40) - 50
    print(f'Carro para {dias} dias: R$ {c_dias:.2f}')
    print(f'\nO custo total da viagem é: R$ {c_cidade + c_noites + c_dias:.2f}')
    gastos_extras = float(input('Gastos extras: R$ '))
    print(f'\nCusto final da viagem: R$ {c_cidade + c_noites + c_dias + gastos_extras:.2f}')

dias = int(input('Carro para quantos dias?: '))
noites = int(input('Quarto para quantas noites?: '))

cidade = input('Para qual dessas cidades você precisa ir? [São Paulo / Porto Alegre / Recife / Manaus]: ').lower()
while cidade != 'são paulo' and cidade != 'porto alegre' and cidade != 'recife' and cidade != 'manaus':
    print('Não temos disponibilidade para esta cidade')
    cidade = input('Para qual dessas cidades você precisa ir? [São Paulo/Porto Alegre/Recife/Manaus]: ').lower()
chama()
