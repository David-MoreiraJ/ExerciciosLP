class televisor:
    def __init__(self,canal,volume):
        self.canal = canal
        self.volume = volume
    
    def mudar_canal(self,novo_canal):
        if 1 <= novo_canal <= 500:
            self.canal = novo_canal
            print(f"Novo canal = {novo_canal}.\n")
        else:
            print("Canal inválido.\n")

    def mudar_volume(self,novo_volume):
        if novo_volume > 0 and novo_volume < 101:
            self.volume = novo_volume
            print(f"Volume = {self.volume}.")
        else:
            print("Volume inválido.")
