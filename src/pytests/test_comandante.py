import pytest
from Comandante import Comandante
from CazaEstelar import CazaEstelar
from Almacen import Almacen
from Repuesto import Repuesto
from Errores import NaveNoComandada, RepuestoDeOtraNave, RepuestoSinStock, RepuestoNoEncontrado

def test_resta_stock():
    comandante = Comandante("Han Solo")
    mi_caza = CazaEstelar("Caza1", 1,"Halcón Milenario", ["Motor"], comandante, 1) 
    
    motor = Repuesto("Motor", "Almacén Espacial 2", stock=5, precio=100)
    almacen = Almacen("Almacén principal", "Tatooine", [motor])

    resultado = comandante.adquirir_repuesto("Motor", almacen, "Halcón Milenario")
    
    assert resultado == True
    assert motor.get_stock() == 4


def test_adquirir_repuesto_nave_no_comandada():
    comandante = Comandante("Luke")
    almacen = Almacen("Almacén principal", "Endor", [])
    
    with pytest.raises(NaveNoComandada):
        comandante.adquirir_repuesto("Motor", almacen, "Caza Tie")


def test_adquirir_repuesto_no_compatible():
    comandante = Comandante("Luke")
    mi_caza = CazaEstelar("Caza2", 1,"Ala-Y", ["Batería"], comandante, 1) 
    almacen = Almacen("Almacén principal", "Endor", [])

    with pytest.raises(RepuestoDeOtraNave):
        comandante.adquirir_repuesto("Motor", almacen, "Ala-Y")


def test_adquirir_repuesto_sin_stock():
    comandante = Comandante("Han Solo")
    mi_caza = CazaEstelar("Caza1", 1,"Halcón Milenario", ["Motor raro"], comandante, 1) 
    
    motor_sin_stock = Repuesto("Motor raro", "Empresa cerrada", stock=0, precio=1000)
    almacen = Almacen("Taller de repuestos", "Tatooine", [motor_sin_stock])

    with pytest.raises(RepuestoSinStock):
        comandante.adquirir_repuesto("Motor raro", almacen, "Halcón Milenario")


def test_adquirir_repuesto_no_existe_en_almacen():
    comandante = Comandante("Han Solo")
    mi_caza = CazaEstelar("Caza1", 1, "Halcón Milenario", ["Motor"], comandante, 1) 
    
    almacen = Almacen("Taller de repuestos", "Tatooine", [Repuesto("Tornillo cápsula de escape", "Almacén espacial 2", stock=10, precio=5)]) 

    with pytest.raises(RepuestoNoEncontrado):
        comandante.adquirir_repuesto("Motor", almacen, "Halcón Milenario")