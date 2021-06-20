class Conta:
    def __init__ (self, titular, __saldo):
        self.titular = titular
        self.__saldo = __saldo
    
    def sacar(self, valor):
        if valor != 0:
            if self.__saldo < valor:
                print(f'Você não tem R$ {valor:.2f} para sacar')
                self.extrato()
            else:
                self.__saldo -= valor
                print(f'Você sacou R$ {valor:.2f}')
                self.extrato()
        else:
            print('Você não pode sacar R$ 0')

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Você depositou R$ {valor:.2f}')
        self.extrato()
    
    def extrato(self):
        self.extrato()

