class Pokemon:
    def __init__ (self, nome, tipo, ataque, defesa):
        self.nomePoke = nome
        self.tipoPoke = tipo
        self.ataquePoke = ataque
        self.defesaPoke = defesa
    
    def atacar(self, valorAtaque):
        self.ataquePoke -= valorAtaque

    def defender(self, valorDefesa):
        self.defesaPoke -= valorDefesa

    def estadoPokemon(self):
        print(f'A pontuação do {self.nomePoke} de ataque é: {self.ataquePoke} e de defesa é: {self.defesaPoke}')
    