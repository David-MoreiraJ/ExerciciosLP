class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def info(self):
        print(f"O nome do funcionário(a) é {self.nome} e ele possui a remuneração de {self.salario:.2f} reais.")
    
    def aumentarSalario(self, aumento):
        self.salario += self.salario * (aumento / 100)
