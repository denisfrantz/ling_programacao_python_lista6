from abc import ABC, abstractmethod

class Item(ABC):
    def __init__ (self, nome, valor):
        self._nome = nome
        self._valor = valor
    
    @abstractmethod
    def empresta (self):
        pass
    
    @abstractmethod
    def retorna (self):
        pass

class Livro(Item):
    def __init__ (self, nome, valor, autor):
        super().__init__(nome, valor)
        self._autor = autor
    
    def empresta (self):
        print ('Emprestando livro')
    
    def retorna (self):
        print ('Devolvendo livro')
    
    def bloqueia (self):
        print ('Bloqueando livro')
    
    def desbloqueia (self):
        print ('Desbloqueando livro')

class ItemRestrito(Item):
    def __init__ (self, nome, valor):
        super().__init__(nome, valor)
    
    def empresta (self):
        print ('Emprestando item restrito')
    
    def retorna (self):
        print ('Devolvendo item restrito')
    
    def alteraNivel (self):
        print ('Alterando nível de acesso')

class Periodico(Livro):
    def __init__ (self, nome, valor, autor):
        super().__init__(nome, valor, autor)
    
    def empresta (self):
        print ('Emprestando livro periódico')
    
    def retorna (self):
        print ('Devolvendo livro periódico')

class Fita(ItemRestrito):
    def __init__ (self, nome, valor):
        super().__init__(nome, valor)
    
    def empresta (self):
        print ('Emprestando fita')
    
    def retorna (self):
        print ('Devolvendo fita')

class SalaEstudo(ItemRestrito):
    def __init__ (self, nome, valor):
        super().__init__(nome, valor)
    
    def empresta (self):
        print ('Emprestando sala de estudo')
    
    def retorna (self):
        print ('Devolvendo sala de estudo')