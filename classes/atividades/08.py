
class PetVirtual:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = 5
        self.felicidade = 5

    def alimentar(self):
        if self.fome > 0:
            self.fome -= 2
           
        if self.fome < 0:
            self.fome = 0
            print(f"{self.nome} foi alimentado! Fome atual: {self.fome}")
        else:
             print(f"{self.nome} já está de barriga cheia!")

    def brincar(self):
        self.felicidade += 2
        self.fome += 1
        print(f"Você brincou com {self.nome}! Felicidade: {self.felicidade} | Fome: {self.fome}")

    def status(self):
        print(f"Nome: {self.nome} | Fome: {self.fome} | Felicidade: {self.felicidade}")
        if self.fome >= 8:
            print(f"Atenção: {self.nome} precisa comer!")

meu_pet = PetVirtual("Pou")

meu_pet.status()

meu_pet.brincar()
meu_pet.brincar()

meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.alimentar()

meu_pet.status()