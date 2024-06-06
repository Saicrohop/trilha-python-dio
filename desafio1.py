saldo = 0
extrato = ""
limite_saque = 500
numero_saques = 0
limite_saques_diarios = 3

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return "Depósito realizado com sucesso!"
    else:
        return "Valor de depósito deve ser positivo!"

def sacar(valor):
    global saldo, extrato, numero_saques, limite_saques_diarios
    if numero_saques < limite_saques_diarios:
        if valor <= saldo and valor <= limite_saque:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            return "Saque realizado com sucesso!"
        elif valor > saldo:
            return "Saldo insuficiente!"
        else:
            return "Valor excede o limite de saque!"
    else:
        return "Limite de saques diários atingido!"

def mostrar_extrato():
    global saldo, extrato
    return extrato + f"Saldo atual: R$ {saldo:.2f}\n"

menu = """
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
"""

while True:
    opcao = input(menu + "Escolha uma opção: ")
    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        print(depositar(valor))
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        print(sacar(valor))
    elif opcao == "3":
        print(mostrar_extrato())
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
