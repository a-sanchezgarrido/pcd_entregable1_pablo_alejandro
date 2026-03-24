from Usuario import Usuario
from Repuesto import Repuesto
from Nave import Nave

class Comandante(Usuario):
    def __init__(self, id):
        super().__init__(id)
        self.__naves_asignadas = []

    def get_naves_asignadas(self):
        return self.__naves_asignadas
    
    def comandante_nueva_nave(self, nave):
        nave.cambiar_comandante(self)

    def consultar_repuesto(self, nombre_repuesto, nombre_nave):
        nave = None
        for i in self.get_naves_asignadas():
            if i.get_nombre() == nombre_nave:
                nave = i
                break
        if nave is None:
            print(f"No comanda ninguna nave llamada '{nombre_nave}'.")
            return False
        if nave.comprobar_repuesto(nombre_repuesto):
            print(f"El repuesto {nombre_repuesto} se encuentra entre los necesarios para la nave")
            return True
        else: 
            print(f"El respuesto {nombre_repuesto} no es necesario para esta nave")
            return False

    def adquirir_repuesto(self, nombre_repuesto, almacen, nombre_nave):
        nave = None
        for i in self.get_naves_asignadas():
            if i.get_nombre() == nombre_nave:
                nave = i
                break
        if nave is None:
            print(f"No comanda ninguna nave llamada '{nombre_nave}'.")
            return False

        if nombre_repuesto not in nave.get_repuestos():
            print(f"El repuesto {nombre_repuesto} no está en la lista de repuestos de {nombre_nave}")
            return False

        for i in almacen.get_catalogo():
            if i.get_nombre() == nombre_repuesto:
                if i.get_stock() > 0:
                    nuevo_stock = i.get_stock() - 1
                    i.set_stock(nuevo_stock)
                    print(f"Repuesto {nombre_repuesto} adquirido correctamente para la nave {nombre_nave}")
                    return True 
                else:
                    print(f"No hay stock de {nombre_repuesto}")
                    return False
        
        print(f"El repuesto {nombre_repuesto} no está en este almacén")
        return False
