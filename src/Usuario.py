from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    @abstractmethod
    def consultar_repuesto(self):
        pass

    @abstractmethod
    def adquirir_repuesto(self):
        pass
