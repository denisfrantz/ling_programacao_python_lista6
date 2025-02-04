from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__ (self, numero, titular, saldo = 0, limite = 1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        
    @abstractmethod
    def atualiza (self, valor):
        pass

class ContaInvestimento(Conta):
    def __init__ (self, numero, titular, saldo = 0, limite = 1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
       
    def atualiza (self, taxa):
        self._saldo += self._saldo * taxa * 5

if __name__ == '__main__':
    ci = ContaInvestimento('123-6', 'Maria', 1000.0)
    ci.atualiza(2)
    print (ci._saldo)