class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print(*self.bucho, sep=", ")

    def digerir(self):
        self.bucho.clear()

# Não é possível fazer um macaco comer outro macaco.
