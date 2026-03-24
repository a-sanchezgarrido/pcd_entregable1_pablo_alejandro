from abc import abstractmethod
from UnidadCombateImperial import UnidadCombateImperial

class Nave(UnidadCombateImperial):
    def __init__(self, idCombate, claveCifrada, nombre, lista_repuestos, comandante):
        super().__init__(idCombate, claveCifrada)
        self.__nombre = nombre
        self.__lista_repuestos = lista_repuestos
        self.__comandante = comandante
        comandante.get_naves_asignadas().append(self)

    def get_nombre(self):
        return self.__nombre
    
    def get_lista_repuestos(self):
        return self.__lista_repuestos
    
    def get_comandante(self):
        return self.__comandante
    
    def cambiar_comandante(self, comandante):
        self.__comandante = comandante
    
    def comprobar_repuesto(self, nombre_repuesto):
        for i in self.get_repuestos():
            if i.get_nombre() == nombre_repuesto:
                return True  
        return False