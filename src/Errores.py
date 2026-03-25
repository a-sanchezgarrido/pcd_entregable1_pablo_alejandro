class RepuestoNoEncontrado(Exception):
    def __init__(self, repuesto, mensaje = "Repuesto no encontrado"):
        super().__init__(mensaje)
        self.__repuesto = repuesto.get_nombre()
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__repuesto}"
    
class RepuestoSinStock(Exception):
    def __init__(self, repuesto, mensaje = "No hay stock para este producto"):
        super().__init__(mensaje)
        self.__repuesto = repuesto.get_nombre()
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__repuesto}"

class RepuestoDeOtraNave(Exception):
    def __init__(self, repuesto, mensaje = "El repuesto que estás buscando no corresponde a esta nave"):
        super().__init__(mensaje)
        self.__repuesto = repuesto.get_nombre()
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__repuesto}"

class NaveNoComandada(Exception):
    def __init__(self, nave, mensaje = "Usted no comanda ninguna nave con ese nombre"):
        super().__init__(mensaje)
        self.__nave = nave.get_nombre()
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__nave}"

