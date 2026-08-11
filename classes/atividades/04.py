
GABARITOS = [
    ["A", "B", "C", "D", "A"],  
    ["B", "B", "A", "C", "D"],  
    ["C", "D", "B", "A", "A"]   
]

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.historico_notas = []  

    def realizar_prova(self, respostas_aluno, gabarito):
        """
        Compara as respostas do aluno com o gabarito e adiciona
        a nota obtida ao histórico de notas.
        """
        acertos = 0
        total_questoes = len(gabarito)
        
        for i in range(total_questoes):
            if respostas_aluno[i] == gabarito[i]:
                acertos += 1
                
        nota_prova = (acertos / total_questoes) * 10
        self.historico_notas.append(nota_prova)
        return nota_prova

    def calcular_media(self):
        """Calcula e retorna a média aritmética do histórico de notas."""
        if not self.historico_notas:
            return 0.0
        return sum(self.historico_notas) / len(self.historico_notas)

    def ver_boletim(self):
        """Exibe o resumo do desempenho do aluno no semestre."""
        media = self.calcular_media()
        situacao = "Aprovado" if media >= 6.0 else "Reprovado"
        
        print("=" * 30)
        print(f"BOLETIM ESCOLAR - {self.nome.upper()}")
        print("=" * 30)
        print(f"Histórico de Notas: {self.historico_notas}")
        print(f"Média Final:        {media:.2f}")
        print(f"Situação:           {situacao}")
        print("=" * 30)

aluno1 = Aluno("Carlos Silva")

respostas_prova1 = ["A", "B", "C", "D", "C"]  # 4 acertos -> Nota 8.0
respostas_prova2 = ["B", "A", "A", "C", "D"]  # 4 acertos -> Nota 8.0
respostas_prova3 = ["A", "D", "B", "C", "A"]  # 3 acertos -> Nota 6.0

aluno1.realizar_prova(respostas_prova1, GABARITOS[0])
aluno1.realizar_prova(respostas_prova2, GABARITOS[1])
aluno1.realizar_prova(respostas_prova3, GABARITOS[2])

aluno1.ver_boletim()