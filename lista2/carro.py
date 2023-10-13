class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  
        self.combustivel = 0

    def andar(self, distancia):
        combustivelNecessario = distancia / self.consumo
        if combustivelNecessario <= self.combustivel:
            self.combustivel -= combustivelNecessario
            print(f"O carro andou por {distancia} km.")
        else:
            print("Não há combustível o suficiente.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros
        print(f"Abastecidos {litros} litros de combustível. Total: {self.combustivel} litros.")
