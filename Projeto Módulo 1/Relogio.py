from random import randint

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
        self.atrasado = False
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def tempoEsgotado(self):
        return (self.horas > 18 or (self.horas == 18 and self.minutos > 0))

    def acordar(self):
        if self.stamina < 50:
            self.atraso = randint(30, 120)
            self.hora_inicial += atraso
        else:
            self.hora_inicial

    acordar(self)