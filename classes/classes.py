class Aluno():
    def __init__(self, nome, idade):
        """Fução de inicialização padrão, deve ser usada para 
criar variáveis que são exclusivas de um objeto"""
        self.nome = nome 
        self.idade = idade 

        print("O aluno" + self.nome + "tem" + str(self.idade) + "anos.")

aluno1 = Aluno("Alberto", 25)
print(aluno1.nome)