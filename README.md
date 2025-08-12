# Sistema-Bancario




MENU = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> """

LIMITE_SAQUE = 500
MAX_SAQUES_DIARIOS = 3

saldo = 0
extrato = []
numero_saques = 0

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("❌ Valor inválido para depósito.")

def sacar(valor):
    global saldo, numero_saques
    if valor <= 0:
        print("❌ Valor inválido para saque.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > LIMITE_SAQUE:
        print(f"❌ Saque excede o limite de R$ {LIMITE_SAQUE:.2f}.")
    elif numero_saques >= MAX_SAQUES_DIARIOS:
        print("❌ Número máximo de saques diários atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

def mostrar_extrato():
    print("\n=========== EXTRATO ===========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("================================")

while True:
    opcao = input(MENU).lower().strip()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            depositar(valor)
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            sacar(valor)
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        print("👋 Obrigado por usar nosso sistema bancário. Até mais!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
