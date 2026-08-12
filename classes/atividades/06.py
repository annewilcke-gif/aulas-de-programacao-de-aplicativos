class Aplicativo:
    def __init__(self, nome, consumo_bateria=100):
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, bateria=100):
        self.ligado = False
        self.bateria = bateria

    def ligar(self):
        self.ligado = True
        print("Celular ligado.")

    def executar_app(self, app):
        
        if not self.ligado:
            print("Não é possível executar um aplicativo com o celular desligado.")
            return

        if self.bateria >= app.consumo_bateria:
            
            self.bateria -= app.consumo_bateria
            
            print(f"Aplicativo '{app.nome}' foi usado! Bateria restante: {self.bateria}%")
        else:
            print(f"Bateria insuficiente para executar '{app.nome}'.")

app1 = Aplicativo("WhatsApp", consumo_bateria=10)
app2 = Aplicativo("Instagram", consumo_bateria=30)

meu_celular = Celular(bateria=100)

meu_celular.ligar()
meu_celular.executar_app(app1)
meu_celular.executar_app(app2)