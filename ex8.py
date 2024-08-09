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
        
    def atualiza (self, valor):
        self._saldo = self._saldo + valor
        
    def deposita (self, quantia):
        self._saldo = self._saldo + quantia
        
if __name__ == '__main__':
    ci = ContaInvestimento('123-6', 'Maria', 1000)
    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print (ci._saldo)