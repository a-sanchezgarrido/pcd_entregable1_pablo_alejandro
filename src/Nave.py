from abc import abstractmethod
from UnidadCombateImperial import UnidadCombateImperial
from Errores import RepuestoDeOtraNave

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
        comandante_viejo = self.get_comandante()
        lista_vieja = comandante_viejo.get_naves_asignadas()        
        for i in range(len(lista_vieja)):
                if lista_vieja[i].get_nombre() == self.get_nombre():
                    del lista_vieja[i]
                    break 
        self.__comandante = comandante
        comandante.get_naves_asignadas().append(self)

    def comprobar_repuesto(self, nombre_repuesto):
        for i in self.get_lista_repuestos():
            if i == nombre_repuesto:
                return True  
        raise RepuestoDeOtraNave(nombre_repuesto)
