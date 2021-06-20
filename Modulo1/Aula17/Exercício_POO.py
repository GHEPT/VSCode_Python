# Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação.

from Conta_Banco import Conta

t1 = Conta('Eduardo', 2000)

while True:
    opcao = int(input('''
    Escolha sua opção:

    [ 1 ] Sacar
    [ 2 ] Depositar
    [ 3 ] Extrato
    [ 4 ] Sair
        
'''))

    if opcao == 1:
        while True:
            saque = float(input('Quanto você quer sacar? R$ '))
            t1.sacar(saque)
            resp = str(input('Quer continuar sacando? [S/N] ').strip().upper()[0])
            if resp == 'N':
                break
    elif opcao == 2:
        while True:
            deposito = float(input('Quanto você quer depositar? R$ '))
            t1.depositar(deposito)
            resp = str(input("Quer continuar depositando? [S/N] ").strip().upper()[0])
            if resp == 'N':
                break
    elif opcao == 3:
        t1.extrato()
    
    elif opcao == 4:
        print('Volte sempre!')
        break
    else:
        print('Opção inválida! Tente novamente.')
