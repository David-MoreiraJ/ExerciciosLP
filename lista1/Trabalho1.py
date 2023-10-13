## QUESTÃO 11 ##

inteiro1 = int(input("Digite o primeiro número inteiro: "))
inteiro2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

print(f"Produto do dobro do primeiro com metade do segundo: {(2*inteiro1) * (inteiro2 / 2) }")
print(f"Soma do triplo do primeiro com o terceiro: {(3 * inteiro1) + (real)}")
print(f"Terceiro elevado ao cubo: {real**3}")

## QUESTÃO 12 ##

altura = float(input("Diga qual é a sua altura, em metros: "))

peso_ideal = (72.7 * altura) - 58

print(f"Seu peso ideal é aproximadamente {peso_ideal:.2f} quilogramas.")

## QUESTÃO 13 ##
altura = float(input("Diga qual sua altura, em metros: "))
sexo = int(input("Digite 1 se você for homem e 2 se for mulher:"))

if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é aproximadamente {peso_ideal:.2f} quilogramas.")
elif sexo == 2:
    peso_idealM = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é aproximadamente {peso_idealM:.2f} quilogramas.")

else:
    print('Comando inválido')

## QUESTÃO 14 ##

peso = float(input("Quantos quilos de peixe João  pegou?"))

if peso > 50.0:
    excedente = peso - 50.0
    multa = excedente * 4
    print(f"Antônio acumulo {multa:.2f} de multa devido ao execente de {excedente:.2f} quilos.")
else:
    print("Não há excedente!")
