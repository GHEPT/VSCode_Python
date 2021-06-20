class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def likes(self):
        return self.__likes

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
    
    def dar_likes(self):
        self.__likes += 1

    @property #quando eu crio um método que referencia um atributo 
    def nome(self):
        return self.__nome
    
    @nome.setter
    def likes(self):
        return self.__likes
    
#criar um filme e uma série
vingadores = Filme('Guerra Infinita', 2018, 160)
vingadores.dar_likes()
vingadores.set_nome('Ultimato')
print(f'{vingadores.get_nome()} - {vingadores.ano} - {vingadores.duracao} - {vingadores.get_likes()}')

friends = Serie('Friends', 1994, 10)
friends.dar_likes()
friends.dar_likes()
#print(f'{friends.get_nome()} - {friends.ano} - {friends.temporadas} - {friends.get_likes()}')

# Getters (obter) and Setters (definir)

# CONTEÚDO DE HOJE: HERANÇA

