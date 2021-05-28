# 03 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

player = int(input('Tente acertar o número que o computador escolheu [de 0 a 10]: '))
comp = randint(0, 10+1)
palpites = 0
if comp == player:
    print(f'Uau!!! Você acertou com apenas 1 palpite!')
elif comp != player:
    while True:
        comp = randint(0, 10+1)
        player = int(input('Tente acertar o número que o computador escolheu [de 0 a 10]: '))
        palpites += 1
        if comp == player:
            palpites += 1
            break
    print(f'Você acertou com {palpites} palpite(s)')
