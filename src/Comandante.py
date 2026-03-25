from Usuario import Usuario
from Repuesto import Repuesto
from Nave import Nave
from Errores import NaveNoComandada, RepuestoSinStock, RepuestoDeOtraNave, RepuestoNoEncontrado

class Comandante(Usuario):
    def __init__(self, id):
        super().__init__(id)
        self.__naves_asignadas = []

    def get_naves_asignadas(self):
        return self.__naves_asignadas
    
    def comandante_nueva_nave(self, nave):
        nave.cambiar_comandante(self)

    def consultar_repuesto(self, nombre_repuesto, nombre_nave):
        try:
            nave = None
            for i in self.get_naves_asignadas():
                if i.get_nombre() == nombre_nave:
                    nave = i
                    break
            if nave is None:
                raise NaveNoComandada(nombre_nave)
            
            nave.comprobar_repuesto(nombre_repuesto)
            print(f"El repuesto {nombre_repuesto} se encuentra entre los necesarios para la nave")
            return True
        
        except NaveNoComandada as e:
            print(e)
            return False
        
        except RepuestoDeOtraNave as e:
            print(e)
            return False

    def adquirir_repuesto(self, nombre_repuesto, almacen, nombre_nave):
        try:
            nave = None
            for i in self.get_naves_asignadas():
                if i.get_nombre() == nombre_nave:
                    nave = i
                    break
            if nave is None:
                raise NaveNoComandada(nombre_nave)
            
            nave.comprobar_repuesto(nombre_repuesto)       # Si no sale salta el error y es cazado por el except
            almacen.comprobar_repuesto(nombre_repuesto)
        
            for i in almacen.get_catalogo():
                if i.get_nombre() == nombre_repuesto:
                    if i.get_stock() > 0:
                        nuevo_stock = i.get_stock() - 1
                        i.set_stock(nuevo_stock)
                        print(f"Repuesto {nombre_repuesto} adquirido correctamente para la nave {nombre_nave}")
                        return True 
                    else:
                        raise RepuestoSinStock(i)
        
        except NaveNoComandada as e:
            print(e)
            return False
        
        except RepuestoDeOtraNave as e:
            print(e)
            return False
        
        except RepuestoNoEncontrado as e:
            print(e)
            return False
        
        except RepuestoSinStock as e:
            print(e)
            return False
