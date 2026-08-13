class OrdemDeServico:
    
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente: str, descricao: str):
        self.cliente = cliente
        self.descricao = descricao

        OrdemDeServico.total_os_criadas += 1
        OrdemDeServico.os_abertas += 1

        self.id_os = OrdemDeServico.total_os_criadas
        self.status = "Aberta"

    def finalizar_os(self):
        if self.status != "Concluída":
            self.status = "Concluída"
            OrdemDeServico.os_abertas -= 1
            print(f"OS #{self.id_os} de {self.cliente} foi concluída com sucesso.")
        else:
            print(f"OS #{self.id_os} já está concluída.")

    @classmethod
    def verificar_os_abertas(cls):
        print(f"Total de Ordens de Serviço abertas no momento: {cls.os_abertas}")
        return cls.os_abertas


os1 = OrdemDeServico("Carlos Silva", "Manutenção na impressora")
os2 = OrdemDeServico("Ana Souza", "Instalação de software de gestão")
os3 = OrdemDeServico("Marcos Lima", "Troca de tela do notebook")


print(f"OS 1 criada - ID: {os1.id_os} | Cliente: {os1.cliente} | Status: {os1.status}")
print(f"OS 2 criada - ID: {os2.id_os} | Cliente: {os2.cliente} | Status: {os2.status}")
print(f"OS 3 criada - ID: {os3.id_os} | Cliente: {os3.cliente} | Status: {os3.status}")

print("---")

OrdemDeServico.verificar_os_abertas()

print("---")

os2.finalizar_os()

print("---")

OrdemDeServico.verificar_os_abertas()