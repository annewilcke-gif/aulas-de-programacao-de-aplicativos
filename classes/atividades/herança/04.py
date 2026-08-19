class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True  
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False


class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas


class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item: ItemBiblioteca):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"'{item.titulo}' foi emprestado com sucesso para {self.nome}.")
        else:
            print(f"Ops! '{item.titulo}' não está disponível no momento.")

    def devolver_item(self, item: ItemBiblioteca):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"'{item.titulo}' foi devolvido por {self.nome}.")
        else:
            print(f"{self.nome} não possui o item '{item.titulo}' emprestado.")

    def ver_historico(self):
        print(f"\n--- Itens em posse de {self.nome} ---")
        if not self.itens_emprestados:
            print("Nenhum item emprestado no momento.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo} (Código: {item.codigo})")

livro1 = Livro("Dom Casmurro", 101, "Machado de Assis", 256)
livro2 = Livro("1984", 102, "George Orwell", 328)

usuario = Usuario("Lucas")

usuario.pegar_item(livro1)

usuario.pegar_item(livro1)

usuario.pegar_item(livro2)
usuario.ver_historico()

usuario.devolver_item(livro1)
usuario.ver_historico()