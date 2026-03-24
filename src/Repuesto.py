class Repuesto():
    def __init__(self, nombre, proveedor, stock, precio):
        self.__nombre= nombre
        self.__proveedor = proveedor
        self.__stock = stock
        self.__precio = precio
    
    def get_nombre(self):
        return self.__nombre
    
    def get_proveedor(self):
        return self.__proveedor
    
    def get_stock(self):
        return self.__stock
    
    def get_precio(self):
        return self.__precio
    