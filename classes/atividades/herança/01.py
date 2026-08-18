class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz um som genérico de animal.")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Canino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) faz: Au Au!")


class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Felino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) faz: Miau!")


class Vaca(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Bovino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) faz: Muuu!")

dog = Cachorro("Rex", "Poodle")
cat = Gato("Felix", "Siamês")
cow = Vaca("Mimosa", "Holandesa")

animais = [dog, cat, cow]

for animal in animais:
    animal.fazer_som()