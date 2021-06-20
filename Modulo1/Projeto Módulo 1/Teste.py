from time import sleep

if __name__ == '__main__':
    nome = str(input('Dê um nome para a sua personagem principal: ').strip().upper())
    
    frase1 = f'\n{nome}'+' é uma bela jovem que mora com sua tia desde que era criança e praticamente não coloca os pés para fora de casa.\nPorém, essa semana sua vida pode mudar!'

    frase2 = f'\nSeu grande amor da adolescência está na cidade e ela terá 7 dias para realizar o sonho de se encontrar com ele, fugirem juntos e viverem felizes para sempre!\nPara conseguir o "vale night" {nome} precisa realizar tarefas...'
    
    frase3 = f'\n\nIMPORTANTE:'

    frase4 = f'\n\n> {nome} deve dormir o necessário para não ficar sem energia para as tarefas\n> A energia também é importante para não ficar doente\n> {nome} só poderá sair de casa após as 18h e deverá decidir quanto tempo ficará fora\n> Se {nome} chegar em casa APÓS 23:59 o jogo acaba\n> Quanto mais tarefas {nome} fizer no dia mais cansada ficará e mais precisará dormir\n> Quanto mais tempo passar fora de casa idem\n> Quanto mais {nome} dormir menos tarefas conseguirá fazer e menores serão suas chances de sair de casa\n> Cuidado para que o amor de {nome} não desista dela'

    frase5 = f'\n\nQue comecem os jogos!'

    frase6 = '''
    OPÇÕES:
    
    [  1 ] Limpar a casa
    [  2 ] Fazer o café
    [  3 ] Fazer um bolo
    [  4 ] Cozinhar
    [  5 ] Regar o jardim
    [  6 ] Aparar a grama
    [  7 ] Lavar o carro da tia
    [  8 ] Passar roupas
    [  9 ] Colher frutas do pomar
    [ 10 ] Fazer um suco
    [ 11 ] Alimentar os animais
    [ 12 ] Limpar a piscina
    [ 13 ] Lavar a louça
    [ 14 ] Passear com o cachorro
    [ 15 ] Se produzir
    [ 16 ] Ir para o encontro
    [ 17 ] Descansar
    [  0 ] Sair
'''
    for i in (frase1):
        print (i, end ='')
        sleep(.06)
    sleep(1)
    
    for i in (frase2):
        print (i, end ='')
        sleep(.06)
    sleep(1)

    for i in (frase3):
        print (i, end ='')
        sleep(.06)
    sleep(1)

    for i in (frase4):
        print (i, end ='')
        sleep(.06)
    sleep(1)

    for i in (frase5):
        print (i, end ='')
        sleep(.06)
    sleep(1)

    print('')
    print('-=' * 50)
    print(frase6)
    opcao = int(input('Escolha uma opção [0 a 18]: ')).strip()



    elif opcao == 10:
        relogio.adicionar_tempo(20)
        personagem.stamina(-5)
        personagem.pontuar(10)

    elif opcao == 11:
        relogio.adicionar_tempo(15)
        personagem.stamina(-5)
        personagem.pontuar(10)
    
    elif opcao == 12:
        relogio.adicionar_tempo(60)
        personagem.stamina(-15)
        personagem.pontuar(20)
    
    elif opcao == 13:
        relogio.adicionar_tempo(15)
        personagem.stamina(-5)
        personagem.pontuar(5)
    
    elif opcao == 14:
        relogio.adicionar_tempo(30)
        personagem.stamina(-10)
        personagem.pontuar(10)
    
    elif opcao == 15:
        relogio.adicionar_tempo(120)
        personagem.stamina(-15)
    
    elif opcao == 16:
        relogio.adicionar_tempo(120)
        personagem.stamina(-20)
    
    elif opçao == 17:
        if 1 <= descanso <= 15:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(2)
            personagem.pontuar(-2)
        elif 15 < descanso <= 30:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(5)
            personagem.pontuar(-5)
        elif 30 < descanso <= 45:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(10)
            personagem.pontuar(-10)
        elif 45 < descanso <= 60:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(15)
            personagem.pontuar(-15)
        elif 60 < descanso <= 75:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(15)
            personagem.pontuar(-15)
        elif 75 < descanso <= 90:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(20)
            personagem.pontuar(-20)
        elif 90 < descanso <= 105:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(20)
            personagem.pontuar(-20)
        elif descanso > 120:
            relogio.adicionar_tempo() += descanso
            personagem.stamina(30)
            personagem.pontuar(-30)
        else:
            print('Opção incorreta. Digite um número inteiro entre 1 e 480: ')
    elif opcao == 0:
        break
    else:
        print('Opção incorreta. Digite um número inteiro entre 0 e 18: ')
