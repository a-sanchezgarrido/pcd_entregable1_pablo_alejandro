class MiImperio():
    def __init__(self, flota, usuario, almacenes):
        self.__flota = flota
        self.__usuario = usuario
        self.__almacenes = almacenes

    def get_lista_flota(self):
        return self.__flota
    
    def get_lista_usuario(self):
        return self.__usuario
    
    def get_lista_almacenes(self):
        return self.__almacenes
    
    