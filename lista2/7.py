from bichinho import Bichinho

tamagushi = Bichinho(nome="Michael")

tamagushi.alterar_fome(30)
tamagushi.alterar_saude(-20)
tamagushi.alterar_idade(6)
tamagushi.alterar_nome("Zezinho")

print("Nome:", tamagushi.retornar_nome())
print("Fome:", tamagushi.retornar_fome())
print("Saúde:", tamagushi.retornar_saude())
print("Idade:", tamagushi.retornar_idade())
print("Humor:", tamagushi.calcular_humor())
