from retangulo import retangulo

a = input("Por favor, informe a medida de base do assoalho em metros\n")
b = input("Agora, informe a altura\n")

retangulo_1 = retangulo(a,b)
#retangulo_1.mudarValor(30,30)
#a, b = retangulo_1.retornar()
#retangulo_1.perimetro()
retangulo_1.assoalho(a,b)
