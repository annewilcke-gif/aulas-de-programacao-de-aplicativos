class OrdemDeServico:
   
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente, descricao):
        self.cliente = cliente
        self.descricao = descricao

        OrdemDeServico.total_os_criadas += 1
        OrdemDeServico.os_abertas += 1

        self.id_os = OrdemDeServico.total_os_criadas
        self.status = "Aberta"

    def finalizar_os(self):
        self.status = "Concluída"
        OrdemDeServico.os_abertas -= 1
        print(f"OS #{self.id_os} foi concluída!")

    def verificar_os_abertas(self):
        print(f"Ordens de serviço abertas no momento: {OrdemDeServico.os_abertas}")


os1 = OrdemDeServico("Carlos", "Manutenção na impressora")
os2 = OrdemDeServico("Ana", "Instalação de software")
os3 = OrdemDeServico("Marcos", "Troca de tela")


os1.verificar_os_abertas()

print("---")

os2.finalizar_os()

print("---")

os1.verificar_os_abertas()