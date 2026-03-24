from Usuario import Usuario
from Repuesto import Repuesto
from Almacen import Almacen

class OperarioAlmacen(Usuario):
    def __init__(self, id):
        super().__init__(id)
    
    def consultar_repuesto_almacen(self, nombre_repuesto, almacen):
        if almacen.comprobar_repuesto(nombre_repuesto):
            print(f"El repuesto {nombre_repuesto} se encuentra en el almacén")
        else:
            print(f"El repuesto {nombre_repuesto} no se encuentra en el almacén")

    def actualizar_stock(self, repuesto, stock):
        nuevo_stock = repuesto.get_stock() + stock
        repuesto.set_stock(nuevo_stock)

    def actualizar_catalogo(self, repuesto, almacen):
        if almacen.comprobar_repuesto(repuesto.get_nombre()):
            for i in almacen.get_catalogo():
                if i.get_nombre() == repuesto.get_nombre():
                    self.actualizar_stock(i, repuesto.get_stock())
                    break 
        else:
            almacen.get_catalogo().append(repuesto)

    def encuentra_repuesto(self, nombre_repuesto, imperio):
        for i in imperio.get_lista_almacenes():
            self.consultar_repuesto_almacen(nombre_repuesto, i)

