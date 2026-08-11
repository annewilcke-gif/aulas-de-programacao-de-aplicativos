class Carro:
    def __init__(self, marca: str, modelo: str, nivel_combustivel: float = 0):
        self.marca = marca
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel
        self.tanque_maximo = 100.0
        self.quilometragem = 0 
    def abastecer(self, quantidade: float):
        if quantidade <= 0:
            print("Informe uma quantidade válida para abastecer.")
            return

        espaco_disponivel = self.tanque_maximo - self.nivel_combustivel

        if quantidade > espaco_disponivel:
            self.nivel_combustivel = self.tanque_maximo
            print(
                f"Tanque cheio! Foram colocados {espaco_disponivel:.1f}L. "
                f"O excesso de {quantidade - espaco_disponivel:.1f}L foi descartado."
            )
        else:
            self.nivel_combustivel += quantidade
            print(f"Abastecido {quantidade:.1f}L com sucesso!")

    def acelerar(self):
        
        consumo = 5.0

        if self.nivel_combustivel >= consumo:
            self.nivel_combustivel -= consumo
            self.quilometragem += 15  
            print(f"Vrummm! O {self.modelo} acelerou e percorreu 15 km.")
        else:
            print(f"Sem combustível suficiente ({self.nivel_combustivel:.1f}L) para acelerar!")

    def painel(self):
        print("\n" + "=" * 30)
        print(f"   PAINEL DO {self.marca.upper()} {self.modelo.upper()}")
        print("=" * 30)
        print(f" Combustível  : {self.nivel_combustivel:.1f} / {self.tanque_maximo} L")
        print(f" Quilometragem: {self.quilometragem} km")
        print("=" * 30 + "\n")

meu_carro = Carro("Toyota", "Corolla", nivel_combustivel=10)

meu_carro.painel()

meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.acelerar()  
meu_carro.abastecer(120)

meu_carro.acelerar()
meu_carro.acelerar()

meu_carro.painel()