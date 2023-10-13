class ContaCorrente:

    def __init__(self, numero_conta, nome_correntista, taxaJuros, saldo = 0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
        juros = 10/100
        self.saldo += self.saldo * juros
        print(f"O saldo atual após os juros é: {self.saldo:.2f} reais")

    def alterar_nome(self, nome_novo):
        self.nome_correntista = nome_novo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} foi concluído. o Novo saldo é : R${self.saldo:.2f}")
        else:
            print("Depósito nulo.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} concluído. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido.")

