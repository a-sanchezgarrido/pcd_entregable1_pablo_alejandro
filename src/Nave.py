from abc import abstractmethod
from UnidadCombateImperial import UnidadCombateImperial

class Nave(UnidadCombateImperial):
    def __init__(self, idCombate, claveCifrada, nombre, repuestos):
        super().__init__(idCombate, claveCifrada)
        self.__nombre = nombre
        self.__repuestos = repuestos

    def get_nombre(self):
        return self.__nombre
    
    def get_repuestos(self):
        return self.__repuestos
    
    @abstractmethod
    def encenderMotor(self):
        return super().encenderMotor()
    