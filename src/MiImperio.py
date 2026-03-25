class MiImperio():
    def __init__(self, flota, usuarios, almacenes):
        self.__flota = flota
        self.__usuarios = usuarios
        self.__almacenes = almacenes

    def get_lista_flota(self):
        return self.__flota
    
    def get_lista_usuarios(self):
        return self.__usuarios
    
    def get_lista_almacenes(self):
        return self.__almacenes
    
    