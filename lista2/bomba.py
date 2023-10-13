class BombaCombustivel:
    def __init__(self, tipo, valorLitro, quantidadeCombustivel):
        self.tipo = tipo
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def porValor(self, valor):
        quantidade = valor / self.valorLitro
        if quantidade > self.quantidadeCombustivel:
            print("Não há combustível o suficiente na bomba.")
            return 0
        else:
            self.quantidadeCombustivel -= quantidade

    def porLitro(self,litros):
        pagamento = litros * self.valorLitro
        if litros > self.quantidadeCombustivel:
            print("Não há combustível o suficiente na bomba.")
            return 0
        else:
            self.quantidadeCombustivel -= litros

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipo = novoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade

    def mostrarQuantidadeCombustivel(self):
        print(f"Quantidade de combustível na bomba: {self.quantidadeCombustivel} litros")

