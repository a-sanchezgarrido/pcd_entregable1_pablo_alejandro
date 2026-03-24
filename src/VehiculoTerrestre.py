from abc import abstractmethod
from UnidadCombateImperial import UnidadCombateImperial

class VehiculoTerrestre(UnidadCombateImperial):
    def __init__(self, idCombate, claveCifrada, nombre, repuestos):
        super().__init__(idCombate, claveCifrada)
    
    @abstractmethod
    def encenderMotor(self):
        return super().encenderMotor()
    