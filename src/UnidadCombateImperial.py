from abc import ABC, abstractmethod

class UnidadCombateImperial(ABC):
    def __init__(self, idCombate, claveCifrada):
        self.__idCombate = idCombate
        self.__claveCifrada = claveCifrada

    def get_idCombate(self):
        return self.__idCombate

    def get_claveCifrada(self):
        return self.__claveCifrada
    
    @abstractmethod
    def encenderMotor(self):
        pass