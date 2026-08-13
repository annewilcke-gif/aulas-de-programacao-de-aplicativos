class Livro:

    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: '{self.titulo}' por {self.autor} {self.paginas} pgs"

    def comparar_tamanho(self, outro_livro):
        if self.paginas > outro_livro.paginas:
            print(
                f"'{self.titulo}' tem mais páginas que '{outro_livro.titulo}'."
            )
        elif self.paginas < outro_livro.paginas:
            print(
                f"'{outro_livro.titulo}' tem mais páginas que '{self.titulo}'."
            )
        else:
            print(
                f"Ambos os livros ('{self.titulo}' e '{outro_livro.titulo}') têm o mesmo número de páginas."
            )

    def diferenca_paginas(self, outro_livro):
        
        diferenca = abs(self.paginas - outro_livro.paginas)

        if self.paginas > outro_livro.paginas:
            print(
                f"'{self.titulo}' tem {diferenca} páginas a mais que '{outro_livro.titulo}'."
            )
        elif self.paginas < outro_livro.paginas:
            print(
                f"'{outro_livro.titulo}' tem {diferenca} páginas a mais que '{self.titulo}'."
            )
        else:
            print(
                f"Não há diferença, ambos os livros têm {self.paginas} páginas."
            )

livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 310)
livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1032)

livro1.diferenca_paginas(livro2)