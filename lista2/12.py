from contaInvestimento import ContaCorrente

joao = ContaCorrente("0000","Joao", 10)

joao.deposito(1000)

i = 0
while i < 5: 
    joao.adicioneJuros()
    i += 1
