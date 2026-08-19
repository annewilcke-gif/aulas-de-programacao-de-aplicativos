class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100

    def acelerar(self):
        if self.combustivel >= 5:
            self.combustivel -= 5
            print(f"O carro acelerou! Combustível restante: {self.combustivel}%")
        else:
            print("Sem combustível suficiente para acelerar!")

    def painel(self):
        print(f"[{self.marca} {self.modelo}] Combustível: {self.combustivel}%")


class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str):
        super().__init__(marca, modelo)
        self.bateria = 100

    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"O carro elétrico acelerou silenciosamente! Bateria restante: {self.bateria}%")
        else:
            print("Bateria insuficiente para acelerar! Por favor, recarregue.")

    def recarregar(self):
        self.bateria = 100
        print("Bateria recarregada para 100%!")

    def painel(self):
        print(f"[{self.marca} {self.modelo}] Bateria: {self.bateria}%")