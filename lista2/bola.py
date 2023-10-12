class bola:
    
    def __init__(self,cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self):
        self.cor = input("Qual a cor da bola?\n")

    def mostrarCor(self):
        print("A cor da bola é "+self.cor+".\n")
