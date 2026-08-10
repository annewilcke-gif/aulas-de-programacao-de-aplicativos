import os
import dinheiro.requisitar_movimentacao as movi


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(saldo):
    print("========================================")
    print("            BANCO DIGITAL               ")
    print("========================================")
    print(f" Saldo Atual: R$ {saldo:.2f}")
    print("----------------------------------------")


def menu_principal():
    saldo = 0  # Saldo inicial

    while True:
        limpar_tela()
        exibir_cabecalho(saldo)
        print(" [1] Depositar")
        print(" [2] Sacar")
        print(" [3] Sair do Sistema")
        print("========================================")
        
        opcao = input(" Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            saldo = movi.processar_deposito(saldo)
            input("\nPressione ENTER para continuar...")
        elif opcao == "2":
            saldo = movi.processar_saque(saldo)
            input("\nPressione ENTER para continuar...")
        elif opcao == "3":
            limpar_tela()
            print("========================================")
            print("  Obrigado por utilizar o Banco Digital! ")
            print("========================================\n")
            break
        else:
            print("\n -> Opção inválida! Escolha entre 1, 2 ou 3.")
            input("\nPressione ENTER para tentar novamente...")

if __name__ == "__main__":
    menu_principal()
