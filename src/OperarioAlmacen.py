from Usuario import Usuario
from Repuesto import Repuesto
from Almacen import Almacen
from Errores import RepuestoNoEncontrado

class OperarioAlmacen(Usuario):
    def __init__(self, id):
        super().__init__(id)
    
    def consultar_repuesto_almacen(self, nombre_repuesto, almacen):
        try:
            almacen.comprobar_repuesto(nombre_repuesto)
            print(f"El repuesto {nombre_repuesto} se encuentra en el almacén {almacen.get_nombre()}")
            return True        
        except RepuestoNoEncontrado as e:
            print(e)
            return False

    def actualizar_stock(self, repuesto, stock):
        nuevo_stock = repuesto.get_stock() + stock
        repuesto.set_stock(nuevo_stock)

    def actualizar_catalogo(self, repuesto, almacen):
        try:
            almacen.comprobar_repuesto(repuesto.get_nombre())
            for i in almacen.get_catalogo():
                if i.get_nombre() == repuesto.get_nombre():
                    self.actualizar_stock(i, repuesto.get_stock())
                    print(f"Stock actualizado para {repuesto.get_nombre()}") 
                    return True
        except RepuestoNoEncontrado:
            almacen.get_catalogo().append(repuesto)
            print(f"Repuesto {repuesto.get_nombre()} añadido al catálogo")
            return True

    def encuentra_repuesto(self, nombre_repuesto, imperio):
        encontrado = False
        for i in imperio.get_lista_almacenes():
            try: 
                i.comprobar_repuesto(nombre_repuesto)
                print(f"El repuesto {nombre_repuesto} se encuentra en el almacén {i.get_nombre()}")
                encontrado = True
            except RepuestoNoEncontrado:
                pass
        if not encontrado:
            print(f"El repuesto {nombre_repuesto} no se encuentra en ningún almacén")
        

