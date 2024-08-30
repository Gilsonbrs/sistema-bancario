class ContaBancaria:
    LIMITE_SALDO = 500  # Define o limite máximo do saldo
    LIMITE_SAQUES = 3  # Define o limite máximo de saques

    def __init__(self, saldo_inicial=0):
        if saldo_inicial > self.LIMITE_SALDO:
            print(f"Saldo inicial não pode exceder R${self.LIMITE_SALDO:.2f}. Ajustando para o limite.")
            saldo_inicial = self.LIMITE_SALDO
        self.saldo = saldo_inicial
        self.transacoes = []  # Lista para armazenar o histórico de transações
        self.num_saques = 0  # Contador de saques realizados

    def deposito(self, valor):
        if valor > 0:
            if self.saldo + valor > self.LIMITE_SALDO:
                print(f"O depósito excede o limite de saldo. O depósito foi ajustado para R${self.LIMITE_SALDO - self.saldo:.2f}.")
                valor = self.LIMITE_SALDO - self.saldo
            self.saldo += valor
            self.transacoes.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if valor > 0:
            if self.num_saques >= self.LIMITE_SAQUES:
                print("Limite de saques atingido. Não é possível realizar mais saques.")
                return
            if valor <= self.saldo:
                self.saldo -= valor
                self.transacoes.append(f"Saque: R${valor:.2f}")
                self.num_saques += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        print("\nExtrato da Conta:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Número de saques restantes: {self.LIMITE_SAQUES - self.num_saques}\n")

def menu():
    print("Sistema Bancário")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

def main():
    conta = ContaBancaria()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            try:
                valor = float(input("Digite o valor do depósito: R$"))
                conta.deposito(valor)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor do saque: R$"))
                conta.saque(valor)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
