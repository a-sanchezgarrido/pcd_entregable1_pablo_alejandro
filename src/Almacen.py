from Errores import RepuestoNoEncontrado

class Almacen():
    def __init__(self, nombre, localizacion, catalogo):
        self.__nombre = nombre
        self.__localizacion = localizacion
        self.__catalogo = catalogo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_localizacion(self):
        return self.__localizacion
    
    def get_catalogo(self):
        return self.__catalogo
    
    def comprobar_repuesto(self, nombre_repuesto):
        for i in self.get_catalogo():
            if i.get_nombre() == nombre_repuesto:
                return True  
        raise RepuestoNoEncontrado(nombre_repuesto)