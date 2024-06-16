# Definições das funções

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    if cpf in [user['cpf'] for user in usuarios]:
        print("Usuário já cadastrado.")
        return False
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    return True

def criar_conta(contas, agencia, usuario_cpf, usuarios):
    usuario = next((user for user in usuarios if user['cpf'] == usuario_cpf), None)
    if not usuario:
        print("CPF não encontrado.")
        return False
    conta_numero = len(contas) + 1
    contas.append({
        'agencia': agencia,
        'numero': conta_numero,
        'usuario': usuario_cpf
    })
    return True

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print("\n======= LISTA DE CONTAS =======")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero']}, CPF do Usuário: {conta['usuario']}")
    print("================================")

# Exemplo de uso das funções
usuarios = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[l] Listar Contas
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")
        criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        usuario_cpf = input("CPF do usuário: ")
        criar_conta(contas, "0001", usuario_cpf, usuarios)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
