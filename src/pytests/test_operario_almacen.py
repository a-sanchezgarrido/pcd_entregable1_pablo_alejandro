import pytest
from OperarioAlmacen import OperarioAlmacen
from Almacen import Almacen
from Repuesto import Repuesto

def test_suma_stock_catalogo():
    repuesto_existente = Repuesto("Motor Especial 1", "Imperial Factory", stock=5, precio=100)
    almacen = Almacen("Base Alfa", "Endor", [repuesto_existente])
    operario = OperarioAlmacen("Chewbacca")
    
    repuesto_nuevo = Repuesto("Motor Especial 1", "Imperial Factory", stock=3, precio=100)
    operario.actualizar_catalogo(repuesto_nuevo, almacen)

    assert len(almacen.get_catalogo()) == 1
    assert almacen.get_catalogo()[0].get_stock() == 8


def test_añade_repuesto_catalogo():
    almacen = Almacen("Base Alfa", "Endor", [])
    operario = OperarioAlmacen("Chewbacca")
    repuesto_nuevo = Repuesto("Tornillo cápsula de escape", "Almacén espacial 2", stock=10, precio=5)

    operario.actualizar_catalogo(repuesto_nuevo, almacen)

    assert len(almacen.get_catalogo()) == 1
    assert almacen.get_catalogo()[0].get_nombre() == "Tornillo cápsula de escape"