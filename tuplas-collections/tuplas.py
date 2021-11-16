from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f">>[Codigo {self._codigo} Saldo {self._saldo}<<]"


conta_do_gui = Conta(15)
conta_da_dani = Conta(47685)

conta_do_gui.deposita(100)
conta_da_dani.deposita(500)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]

print(contas)


# Modulo 2 - Aula 2
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_gui, conta_da_dani]

deposita_para_todas(contas)
print(contas[0], contas[1])

guilherme = ('Guilherme', 37, 1981)  # tupla


## HERANçA E POLIMOFISMO


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)

conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()


class ContaInvestimento(Conta):
    pass


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for indice, idade in enumerate(idades):
    print(indice, " x ", idade)

sorted(idades)

list(reversed(idades))

sorted(idades, reverse=True)

list(reversed(sorted(idades)))
