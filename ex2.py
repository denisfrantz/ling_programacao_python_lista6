from abc import ABC, abstractmethod

class Conta(ABC):
    @abstractmethod
    def atualiza (self):
        pass