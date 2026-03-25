class RepuestoNoEncontrado(Exception):
    def __init__(self, nombre_repuesto, mensaje = "Repuesto no encontrado"):
        super().__init__(mensaje)
        self.__repuesto = nombre_repuesto
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__repuesto}"
    
class RepuestoSinStock(Exception):
    def __init__(self, nombre_repuesto, mensaje = "No hay stock para este producto"):
        super().__init__(mensaje)
        self.__repuesto = nombre_repuesto
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__repuesto}"

class RepuestoDeOtraNave(Exception):
    def __init__(self, nombre_repuesto, mensaje = "El repuesto que estás buscando no corresponde a esta nave"):
        super().__init__(mensaje)
        self.__repuesto = nombre_repuesto
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__repuesto}"

class NaveNoComandada(Exception):
    def __init__(self, nombre_nave, mensaje = "Usted no comanda ninguna nave con ese nombre"):
        super().__init__(mensaje)
        self.__nave = nombre_nave
        self.__mensaje = mensaje

    def __str__(self):
        return f"{self.__mensaje}: {self.__nave}"

