class Animal:
    def __init__(self, nome: str, especie: str, idade: int = 0):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} faz um som genérico.")

    def aniversario(self):
        self.idade += 1
        print(f"O {self.nome} fez {self.idade} anos!")

class Cachorro(Animal):
    def __init__(self, nome: str, idade: int = 0): 
        super().__init__(nome, "Cachorro", idade)

    def emitir_som(self):
        print(f"{self.nome} diz: Au au!")

class Gato(Animal):
    def __init__(self, nome: str, idade: int = 0):
        super().__init__(nome, "Gato", idade)

    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")


class Papagaio(Animal):
    def __init__(self, nome: str, idade: int = 0):
        super().__init__(nome, "Papagaio", idade)

    def emitir_som(self):
        print(f"{self.nome} diz: Dá o pé, louro!")

dog = Cachorro(nome="Rex", idade=2)
cat = Gato(nome="Mingau")
bird = Papagaio(nome="Loro", idade=5)

animais = [dog, cat, bird]

for animal in animais:
    print(f"\n--- Interagindo com {animal.nome} ({animal.especie}) ---")
    animal.emitir_som()
    animal.aniversario()
    animal.aniversario()