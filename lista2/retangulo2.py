class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.inicial = Ponto(0,0)

    def centro(self):
        centro_x = self.largura / 2
        centro_y = self.altura / 2
        pontoCentral = Ponto(centro_x, centro_y)
        Ponto.imprimir(pontoCentral)

    def move(self, dx, dy):
        self.inicial.move(dx, dy)
        print(f'({self.inicial.x}, {self.inicial.y})')
