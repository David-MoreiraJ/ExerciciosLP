from bichinho3 import Bichinho

def mostrar_menu():
    print("Menu:")
    print("1. Alimentar o bichinho")
    print("2. Brincar com o bichinho")
    print("3. Alterar nome do bichinho")
    print("100. (porta escondida)")
    print("0. Sair")

nome_bichinho = input("Digite o nome do bichinho: ")
bichinho = Bichinho(nome_bichinho)
bichinho.alterar_fome(50)
bichinho.alterar_saude(-20)
bichinho.alterar_idade(6)

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        quantidade = int(input("Digite a quantidade de comida: "))
        bichinho.alimentar(quantidade)
    elif escolha == "2":
        tempo = int(input("Digite o tempo de brincadeira: "))
        bichinho.brincar(tempo)
    elif escolha == "3":
        novo_nome = input("Digite o novo nome do bichinho: ")
        bichinho.alterar_nome(novo_nome)
    elif escolha == "100":
        print(bichinho)  # Aciona a "porta escondida" para mostrar os valores exatos dos atributos
    elif escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
