class CofreDigital:

    def __init__(self, titular, senha):
        self.titular = titular
        self.__senha = senha 
        self.__saldo = 0.0 
    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depositado: R$ {valor:.2f}")

    def sacar(self, valor, senha_informada):
       
        if senha_informada != self.__senha:
            print("Senha incorreta! Acesso negado.")
            return

        
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado! Saldo atual: R$ {self.__saldo:.2f}")
        else:
            print("Saldo insuficiente!")


meu_cofre = CofreDigital("Mariana", "1234")

meu_cofre.depositar(100)  
meu_cofre.sacar(30, "9999")  
meu_cofre.sacar(30, "1234") 
print("\n--- TENTANDO ALTERAR DIRETO (ENCAPSULAMENTO) ---")

meu_cofre.__saldo = 1000  
meu_cofre.__senha = "0000"  
meu_cofre.sacar(10, "1234")  