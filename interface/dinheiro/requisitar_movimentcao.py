import dinheiro.movimentacao as movi


def processar_deposito(saldo_atual):
    print("\n--- PROCESSANDO DEPÓSITO ---")
    try:
        valor = float(input("Digite o valor que deseja depositar: R$ "))
        novo_saldo = movi.adicionar_dinheiro(saldo_atual, valor)
        return novo_saldo
    except ValueError:
        print("-> Erro: Por favor, digite um número válido.")
        return saldo_atual

def processar_saque(saldo_atual):
    print("\n--- PROCESSANDO SAQUE ---")
    try:
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        novo_saldo = movi.retirar_dinheiro(saldo_atual, valor)
        return novo_saldo
    except ValueError:
        print("-> Erro: Por favor, digite um número válido.")
        return saldo_atual