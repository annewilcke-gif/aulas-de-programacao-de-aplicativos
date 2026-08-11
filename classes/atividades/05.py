class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade: int) -> bool:
        """Reduz a quantidade de itens no estoque se houver disponibilidade."""
        if quantidade <= 0:
            print("A quantidade para compra deve ser maior que zero.")
            return False

        if quantidade > self.estoque:
            print(
                f"Estoque insuficiente de '{self.nome}'! "
                f"Disponível: {self.estoque} unidades | Solicitado: {quantidade}."
            )
            return False

        self.estoque -= quantidade
        return True


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = [] 
    def adicionar_ao_carrinho(self, produto: Produto, quantidade: int):
        """Valida o estoque do produto e adiciona a tupla (produto, quantidade) ao carrinho."""
        
        if produto.reduzir_estoque(quantidade):
            self.produtos.append((produto, quantidade))
            print(f"Adicionado ao carrinho: {quantidade}x {produto.nome}")

    def calcular_total(self) -> float:
        """Calcula a soma dos preços de todos os itens no carrinho."""
        return sum(produto.preco * qtd for produto, qtd in self.produtos)

    def mostrar_carrinho(self):
        """Percorre e exibe todos os itens do carrinho e o valor total."""
        print("\n" + "=" * 50)
        print("           CARRINHO DE COMPRAS")
        print("=" * 50)

        if not self.produtos:
            print(" O carrinho está vazio.")
            print("=" * 50 + "\n")
            return

        for item in self.produtos:
            produto, quantidade = item
            subtotal = produto.preco * quantidade
            print(
                f"- {produto.nome:<20} | R$ {produto.preco:>6.2f} x {quantidade:>2} "
                f"= R$ {subtotal:>7.2f}"
            )

        print("-" * 50)
        print(f" TOTAL A PAGAR: R$ {self.calcular_total():.2f}")
        print("=" * 50 + "\n")

p1 = Produto("Notebook", 3500.00, estoque=5)
p2 = Produto("Mouse Sem Fio", 80.00, estoque=10)
p3 = Produto("Teclado Mecânico", 250.00, estoque=2)

meu_carrinho = CarrinhoDeCompras()

meu_carrinho.adicionar_ao_carrinho(p1, quantidade=1)
meu_carrinho.adicionar_ao_carrinho(p2, quantidade=2)

meu_carrinho.adicionar_ao_carrinho(p3, quantidade=5)

meu_carrinho.adicionar_ao_carrinho(p3, quantidade=2)

meu_carrinho.mostrar_carrinho()

print("--- ESTOQUE ATUALIZADO NO ALMOXARIFADO ---")
print(f"{p1.nome}: {p1.estoque} un")
print(f"{p2.nome}: {p2.estoque} un")
print(f"{p3.nome}: {p3.estoque} un")