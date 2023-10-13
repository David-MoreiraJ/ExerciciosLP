class Bichinho:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alimentar(self, quantidade):
        novoValor = self.fome - (self.saude * (quantidade / 10))
        if novoValor < 0:
            self.fome = 0
        else:
            self.fome = novoValor
    
    def brincar(self, tempo):
        novoValor = self.saude + (self.saude * (tempo / 10))
        if novoValor > 100:
            self.saude = 100
        else:
            self.saude = novoValor


    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, valor):
        self.fome += valor
        if self.fome < 0:
            self.fome = 0
        elif self.fome > 100:
            self.fome = 100

    def alterar_saude(self, valor):
        self.saude += valor
        if self.saude < 0:
            self.saude = 0
        elif self.saude > 100:
            self.saude = 100

    def alterar_idade(self, anos):
        self.idade += anos

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        humor = (self.saude - self.fome)
        return humor

    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}"
