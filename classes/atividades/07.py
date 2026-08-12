class Bicicleta:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.velocidade = 0  

    def pedalar(self):
        
        if self.velocidade + 5 <= 60:
            self.velocidade += 5
        else:
            self.velocidade = 60
            
        print(f"A bike {self.modelo} acelerou! Velocidade: {self.velocidade} km/h")

    def frear(self):
        
        if self.velocidade > 0:
            self.velocidade -= 5
            print(f"Reduzindo... Velocidade: {self.velocidade} km/h")
        else:
            print("A bicicleta já está totalmente parada!")

    def radar_de_velocidade(self):
        print(f"Velocidade atual: {self.velocidade} km/h")


minha_bike = Bicicleta("Caloi")

minha_bike.pedalar()
minha_bike.pedalar()

minha_bike.radar_de_velocidade()

minha_bike.frear()
minha_bike.frear()
minha_bike.frear()