from Nave import Nave

class CazaEstelar(Nave):
    def __init__(self, idCombate, claveCifrada, nombre, repuestos, comandante, dotacion):
        super().__init__(idCombate, claveCifrada, nombre, repuestos, comandante)
        self.__dotacion = dotacion
    
    def get_dotacion(self):
        return self.__dotacion
    
