# Escopo do projeto

# Em grupos de 2 ou 3 pessoas, crie um jogo de ficção interativa que simule a rotina diária de um personagem. Você pode escolher entre rotinas matinais, rotinas de trabalho, rotinas de estudos, entre outras. A ideia do jogo é que o jogador faça as escolhas para o seu personagem e o conduza durante o seu dia. Cada escolha irá gerar uma consequência diferente para o seu personagem. O jogo acaba quando o dia do seu personagem acabar. Você será responsável por determinar o inicio e término do dia do seu personagem, além de avançar o tempo a cada escolha.
from random import randint

while True:
        print('-=' * 40)
        print('São '+str(relogio)+' do dia '+str(dia)'. 
        print('Você tem um encontro com o Príncipe às 18:00.')
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Tomar remédio")
        print("6 - Comprar remédio")
        print("7 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")

