class Almacen():
    def __init__(self, nombre, localizacion, catalogo):
        self.__nombre= nombre
        self.__localizacion = localizacion
        self.__catalogo = catalogo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_localizacion(self):
        return self.__localizacion
    
    def get_catalogo(self):
        return self.__catalogo
    
    