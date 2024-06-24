from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False
        elif valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False
        else:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            print(f"Saque: R$ {valor:.2f} realizado com sucesso.")
            return True

    def depositar(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False
        else:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
            print(f"Depósito: R$ {valor:.2f} realizado com sucesso.")
            return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if valor > self._limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False
        return super().sacar(valor)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


class Transacao(ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def registrar(self, conta):
        conta.sacar(self.valor)


class Deposito(Transacao):
    def registrar(self, conta):
        conta.depositar(self.valor)


# Exemplo de uso
cliente = PessoaFisica("João da Silva", "1980-05-15", "123.456.789-00", "Rua Exemplo, 123 - Cidade/Estado")
conta_do_joao = ContaCorrente(1, cliente)
cliente.adicionar_conta(conta_do_joao)

cliente.realizar_transacao(conta_do_joao, Deposito(100))
cliente.realizar_transacao(conta_do_joao, Saque(50))

# Imprimindo o extrato
for transacao in conta_do_joao.historico.transacoes:
    print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
