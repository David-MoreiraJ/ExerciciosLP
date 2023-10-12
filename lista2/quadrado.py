class quadrado:

    def __init__(self,lado):
        self.lado = lado

    def mudarLado(self):
        self.lado = input("Qual o valor do lado do quadrado?\n")

    def retornarLado(self):
        print(f"O lado vale {self.lado}.\n")

    def area(self):
        area = int(self.lado) ** 2 
        print(f"A área do quadrado vale {area} \n")
