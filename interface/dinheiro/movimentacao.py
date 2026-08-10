def adicionar_dinheiro(saldo_atual, valor):
    if valor > 0:
        novo_saldo = saldo_atual + valor
        print(f"Sucesso: R$ {valor:.2f} adicionados.")
        return novo_saldo
    else:
        print("Erro: O valor a adicionar deve ser maior que zero.")
        return saldo_atual

def retirar_dinheiro(saldo_atual, valor):
    if valor <= 0:
        print("Erro: O valor a retirar deve ser maior que zero.")
        return saldo_atual
    elif valor > saldo_atual:
        print("Erro: Saldo insuficiente para realizar a retirada.")
        return saldo_atual
    else:
        novo_saldo = saldo_atual - valor
        print(f"Sucesso: R$ {valor:.2f} retirados.")
        return novo_saldo