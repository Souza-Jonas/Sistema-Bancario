import textwrap

def menu():
    menu = """\
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q]  Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito:\tR$ {valor:.2f}")
        print("\n✅ Depósito realizado com sucesso!")
    else:
        print("\n⚠️ Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n⚠️ Valor inválido para saque.")
    elif valor > saldo:
        print("\n⚠️ Saldo insuficiente.")
    elif valor > limite:
        print("\n⚠️ Valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("\n⚠️ Limite de saques diários atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        numero_saques += 1
        print("\n✅ Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\n".join(extrato))
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n⚠️ Usuário já cadastrado.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("\n✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do titular: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n✅ Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("\n⚠️ Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500
    AGENCIA = "0001"

    saldo = 0
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        match opcao:
            case "d":
                valor = float(input("Valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            case "s":
                valor = float(input("Valor do saque: "))
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=LIMITE_VALOR,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )

            case "e":
                exibir_extrato(saldo, extrato=extrato)

            case "nu":
                criar_usuario(usuarios)

            case "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)

            case "lc":
                listar_contas(contas)

            case "q":
                print("\n👋 Saindo do sistema. Até logo!")
                break

            case _:
                print("\n⚠️ Opção inválida. Tente novamente.")

main()
