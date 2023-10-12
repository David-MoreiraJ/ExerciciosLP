from conta import ContaCorrente

conta = ContaCorrente("123456789", "David")

print(f"Número da Conta: {conta.numero_conta}, Nome do Correntista: {conta.nome_correntista}, Saldo: R${conta.saldo:.2f}")

conta.alterar_nome("Carlinhos")

conta.deposito(1000)

conta.saque(200)

conta.saque(2000)

print(f"Número da Conta: {conta.numero_conta}, Nome do Correntista: {conta.nome_correntista}, Saldo: R${conta.saldo:.2f}")
