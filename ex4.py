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
    
class ContaCorrente(Conta):
    def atualiza (self, valor):
        self._saldo = self._saldo + valor  

class ContaPoupanca(Conta):
    def atualiza (self, valor):
        self._saldo = self._saldo + valor  

if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)

    cc.atualiza(0.01)
    cp.atualiza(0.01)
    print (cc._saldo)
    print (cp._saldo)