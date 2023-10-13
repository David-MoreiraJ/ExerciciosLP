from bomba import BombaCombustivel

bomba = BombaCombustivel("Gasolina", 5.80, 1000)  
bomba.mostrarQuantidadeCombustivel()

bomba.porValor(50)
bomba.mostrarQuantidadeCombustivel()

bomba.alterarValor(6.00)
bomba.porLitro(10)
bomba.mostrarQuantidadeCombustivel()

bomba.alterarQuantidadeCombustivel(500)
bomba.mostrarQuantidadeCombustivel()
