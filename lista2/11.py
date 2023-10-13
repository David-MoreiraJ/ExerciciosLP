from carro import Carro

jeep = Carro(12)  
jeep.adicionarGasolina(18)  
jeep.andar(100)  
print(f"Restam {jeep.obterGasolina()} litros de combustível.")

corola = Carro(20)
corola.adicionarGasolina(30)
corola.andar(10000)
print(f"Restam {corola.obterGasolina()} litros de combustível.")

