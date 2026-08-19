class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome} | CPF: {self.cpf} | Salário: R$ {self.salario:.2f}")

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def receber_bonificacao(self):
        self.salario += self.salario * 0.10
        print(f" Parabéns {self.nome}! Bonificação de 10% aplicada no setor de {self.setor}.")


f1 = Funcionario("João Silva", "123.456.789-00", 3000)
f1.exibir_dados()

f1.aumentar_salario(10)  
f1.exibir_dados()

print("---")

g1 = Gerente("Maria Souza", "987.654.321-11", 6000, "TI")
g1.exibir_dados()

g1.receber_bonificacao()  
g1.exibir_dados()