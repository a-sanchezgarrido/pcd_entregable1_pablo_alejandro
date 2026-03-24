from Usuario import Usuario
from Repuesto import Repuesto
from Nave import Nave

class Comandante(Usuario):
    def __init__(self, id):
        super().__init__(id)
    
    def consultar_repuesto(self, nombre_repuesto, nave):
        if nave.comprobar_repuesto(nombre_repuesto):
            print(f"El repuesto {nombre_repuesto} se encuentra en la nave")

    def adquirir_repuesto(self):
        pass

