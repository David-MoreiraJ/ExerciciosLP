class Tamagotchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alteraNome(self, novoNome):
        self.nome = novoNome

    def alteraFome(self, novaFome):
        if novaFome < 0:
            self.fome = 0
            
        elif novaFome > 100:
            self.fome = 100

        else:
            self.fome = novaFome

    def alteraSaude(self, novaSaude):
        if saude < 0:
            self.saude = 0
        
        if saude > 100:
            self.saude = 100

        else:
            self.saude = novaSaude

    def alteraIdade(self, novaIdade):
        self.idade = novaIdade

    def retornaNome(self):
        print(self.nome)

    def retornaFome(self):
        print(self.fome)

    def retornaSaude(self):
        print(self.saude)

    def retornaIdade(self):
        print(self.idade)

    def calculaHumor(self):
        return (-(self.fome)+100 + self.saude)/2
    
    def come(self, qtdComida):
        if qtdComida <= self.fome:
            self.fome =- qtdComida
        else:
            print('Assim o Tamagotchi vai explodir!!!')

    def brinca(self, tempoBrinca):
        if tempoBrinca <= self.tedio:
            self.tedio -= tempoBrinca
        else:
            print('Assim o Tamagotchi vai explodir de felicidade!')
    
    def str(self):
        print('Nome: ', self.retornaNomme())
        print('Idade: ', self.retornaIdade())
        print('Fome: ', self.retornaFome())
        print('Saude: ', self.retornaSaude())
        print('Humor: ', self.retornaHumor())

nome = str(input('Digite o nome do seu Tamagotchi: '))
fome = int(input('Digite a fome do seu Tamagotchi (0 a 100): '))
saude = int(input('Digite a saúde do seu Tamagotchi (0 a 100): '))
idade = int(input('Digite a idade do seu Tamagotchi: '))

tgc = Tamagotchi(nome, fome, saude, idade)

