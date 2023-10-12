from pessoas import Pessoa

pessoa = Pessoa("David", 22, 62, 172)

print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nPeso: {pessoa.peso}\nAltura: {pessoa.altura}\n")

pessoa.envelhecer(10)

pessoa.engordar(3)

pessoa.emagrecer(2)

pessoa.crescer(4)

print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nPeso: {pessoa.peso}\nAltura: {pessoa.altura}\n")
