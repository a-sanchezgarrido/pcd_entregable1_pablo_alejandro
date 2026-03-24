from Nave import Nave

class Estacion(Nave):
    def __init__(self, idCombate, claveCifrada, nombre, repuestos, tripulacion, pasaje, ubicacion):
        super().__init__(idCombate, claveCifrada, nombre, repuestos)
        self.__tripulacion = tripulacion
        self.__pasaje = pasaje
        self.__ubicacion = ubicacion

    def get_tripulacion(self):
        return self.__tripulacion
    
    def get_pasaje(self):
        return self.__pasaje
    
    def get_ubicacion(self):
        return self.__ubicacion