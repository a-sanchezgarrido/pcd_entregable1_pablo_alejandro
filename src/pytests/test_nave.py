import pytest
from CazaEstelar import CazaEstelar
from Comandante import Comandante

def test_cambiar_comandante():
    comandante_viejo = Comandante("Obi-Wan")
    comandante_nuevo = Comandante("Anakin")
    mi_caza = CazaEstelar("Caza1", 1,"Estrellita", ["Motor", "Rueda"], comandante_viejo, 1) 

    mi_caza.cambiar_comandante(comandante_nuevo)

    assert len(comandante_viejo.get_naves_asignadas()) == 0
    assert len(comandante_nuevo.get_naves_asignadas()) == 1
    assert mi_caza.get_comandante() == comandante_nuevo


def test_comprobar_repuesto_necesario():
    comandante_aux = Comandante("Julio")
    mi_caza = CazaEstelar("Caza2", 2, "Ala-X", ["Cañón Láser"], comandante_aux, 2)
    
    assert mi_caza.comprobar_repuesto("Cañón Láser") == True