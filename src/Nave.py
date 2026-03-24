from abc import abstractmethod
from UnidadCombateImperial import UnidadCombateImperial

class Nave(UnidadCombateImperial):
    def __init__(self, idCombate, claveCifrada, nombre, repuestos, comandante):
        super().__init__(idCombate, claveCifrada)
        self.__nombre = nombre
        self.__repuestos = repuestos
        self.__comandante = comandante

    def get_nombre(self):
        return self.__nombre
    
    def get_repuestos(self):
        return self.__repuestos
    
    def get_comandante(self):
        return self.__comandante
    
    def cambiar_comandante(self, comandante):
        self.__comandante = comandante
    
    @abstractmethod
    def encenderMotor(self):
        return super().encenderMotor()
    