from Nave import Nave

class NaveEstelar(Nave):
    def __init__(self, idCombate, claveCifrada, nombre, repuestos, tripulacion, pasaje, clase):
        super().__init__(idCombate, claveCifrada, nombre, repuestos)
        self.__tripulacion = tripulacion
        self.__pasaje = pasaje
        self.__clase = clase

    def get_tripulacion(self):
        return self.__tripulacion
    
    def get_pasaje(self):
        return self.__pasaje
    
    def get_clase(self):
        return self.__clase