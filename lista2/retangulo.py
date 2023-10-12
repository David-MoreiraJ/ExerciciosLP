
class retangulo:

    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def mudarValor(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
    
    def retornar(self):
        return(self.base, self.altura)

    def perimetro(self):
        perimetro = int(self.base) + int(self.altura)

    def assoalho(self,base,altura):
        pisos = (int(base) * int(altura)) / 0.9
        rodape = (int(base) * 2) + (int(altura) * 2) / 10

        print(f"O projeto precisará de {pisos} pisos e {rodape} rodapés.\n")
