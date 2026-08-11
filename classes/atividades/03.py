class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_cheque_especial = 500.0  

    def saldo_disponivel(self) -> float:
        """Retorna o total disponível para uso (Saldo atual + Limite)."""
        return self.saldo + self.limite_cheque_especial

    def adicionar_saldo(self, valor: float):
        if valor <= 0:
            print("O valor para depósito/transferência deve ser positivo.")
            return False
        self.saldo += valor
        print(f"R$ {valor:.2f} depositados/recebidos na conta de {self.titular}.")
        return True

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return False

        if valor > self.saldo_disponivel():
            print(
                f" Transação bloqueada para {self.titular}! "
                f"Valor de R$ {valor:.2f} excede o limite disponível de R$ {self.saldo_disponivel():.2f}."
            )
            return False

        self.saldo -= valor
        print(f"Saque/Débito de R$ {valor:.2f} realizado na conta de {self.titular}.")
        return True

    def transferir(self, valor: float, conta_destino: "ContaBancaria"):
        print("\n" + "=" * 55)
        print(f"INICIANDO TRANSFERÊNCIA DE R$ {valor:.2f} DE {self.titular.upper()} PARA {conta_destino.titular.upper()}")
        print("=" * 55)

        print("--- SALDO ANTES DA TRANSFERÊNCIA ---")
        self.exibir_saldo()
        conta_destino.exibir_saldo()
        print("-" * 35)

        if self.sacar(valor):
            
            conta_destino.adicionar_saldo(valor)
            print(" Transferência concluída com sucesso!")
        else:
            print(" Transferência cancelada por falta de saldo/limite!")

        print("\n--- SALDO DEPOIS DA TRANSFERÊNCIA ---")
        self.exibir_saldo()
        conta_destino.exibir_saldo()
        print("=" * 55 + "\n")

    def exibir_saldo(self):
        status_limite = f" (Usando R$ {abs(self.saldo):.2f} do limite)" if self.saldo < 0 else ""
        print(
            f"Conta: {self.titular:<10} | Saldo: R$ {self.saldo:>8.2f} | "
            f"Disponível p/ uso: R$ {self.saldo_disponivel():>8.2f}{status_limite}"
        )

conta_ana = ContaBancaria("Ana", saldo_inicial=200.0)
conta_bruno = ContaBancaria("Bruno", saldo_inicial=100.0)

conta_ana.transferir(500.0, conta_bruno)

conta_ana.transferir(300.0, conta_bruno)