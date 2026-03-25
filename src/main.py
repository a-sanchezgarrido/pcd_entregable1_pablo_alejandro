
from Repuesto import Repuesto
from Almacen import Almacen
from Comandante import Comandante
from OperarioAlmacen import OperarioAlmacen
from EstacionEspacial import EstacionEspacial
from NaveEstelar import NaveEstelar
from CazaEstelar import CazaEstelar
from MiImperio import MiImperio
from Ubicacion import Ubicacion
from Clase_Nave import Clase_Nave
from Errores import NaveNoComandada, RepuestoDeOtraNave, RepuestoNoEncontrado, RepuestoSinStock


if __name__ == "__main__":

    print("--- CREACIÓN DE REPUESTOS ---")
    r1 = Repuesto("Motor", "Kuat", 5, 1200)
    r2 = Repuesto("Laser", "Corellia", 3, 500)
    r3 = Repuesto("Escudo", "Sienar", 0, 900)
    r4 = Repuesto("Radar", "Incom", 2, 300)
    r5 = Repuesto("Hyperdrive", "Kuat", 1, 2500)

    print("Repuestos creados:")
    print(r1.get_nombre(), r1.get_stock(), r1.get_precio())
    print(r2.get_nombre(), r2.get_stock(), r2.get_precio())
    print(r3.get_nombre(), r3.get_stock(), r3.get_precio())
    print(r4.get_nombre(), r4.get_stock(), r4.get_precio())
    print(r5.get_nombre(), r5.get_stock(), r5.get_precio())

    print("\n--- CREACIÓN DE ALMACENES ---")
    almacen1 = Almacen("Almacen Central", "Endor", [r1, r2, r3])
    almacen2 = Almacen("Almacen Exterior", "Raimos", [r4, r5])

    print("Almacenes creados:")
    print(almacen1.get_nombre(), "-", almacen1.get_localizacion())
    print(almacen2.get_nombre(), "-", almacen2.get_localizacion())

    print("\n--- CREACIÓN DE USUARIOS ---")
    comandante1 = Comandante("CMD-01")
    comandante2 = Comandante("CMD-02")
    operario1 = OperarioAlmacen("OP-01")

    print("Usuarios creados:")
    print("Comandante 1:", comandante1.get_id())
    print("Comandante 2:", comandante2.get_id())
    print("Operario:", operario1.get_id())

    print("\n--- CREACIÓN DE NAVES ---")
    estacion = EstacionEspacial("U-001", 1234, "Base Endor", ["Motor", "Laser", "Escudo"], comandante1, 200, 50, Ubicacion.ENDOR)

    nave_estelar = NaveEstelar("U-002", 5678, "Destructor Eclipse", ["Motor", "Hyperdrive", "Radar"], comandante1, 500, 100, Clase_Nave.ECLIPSE)

    caza = CazaEstelar("U-003", 9999, "TIE Avanzado", ["Laser", "Radar"], comandante2, 1)

    print("Naves creadas:")
    print(estacion.get_nombre())
    print(nave_estelar.get_nombre())
    print(caza.get_nombre())

    print("\n--- CREACIÓN DEL SISTEMA MiIMPERIO ---")
    imperio = MiImperio(
        [estacion, nave_estelar, caza],
        [comandante1, comandante2, operario1],
        [almacen1, almacen2]
    )

    print("MiImperio creado correctamente")
    print("Número de naves:", len(imperio.get_lista_flota()))
    print("Número de usuarios:", len(imperio.get_lista_usuarios()))
    print("Número de almacenes:", len(imperio.get_lista_almacenes()))

    print("\n--- PRUEBAS DE CONSULTA ---")
    comandante1.consultar_repuesto("Motor", "Base Endor")
    comandante1.consultar_repuesto("Hyperdrive", "Destructor Eclipse")
    operario1.consultar_repuesto_almacen("Laser", almacen1)
    operario1.encuentra_repuesto("Radar", imperio)

    print("\n--- PRUEBAS DE ACTUALIZACIÓN DE ALMACÉN ---")
    nuevo_repuesto = Repuesto("Comunicador", "Sienar", 4, 150.0)
    operario1.actualizar_catalogo(nuevo_repuesto, almacen1)
    operario1.actualizar_stock(r1, 2)
    print("Stock de Motor tras actualización:", r1.get_stock())

    print("\n--- PRUEBA DE CAMBIO DE COMANDANTE ---")
    print("Naves de comandante2 antes:", len(comandante2.get_naves_asignadas()))
    comandante2.comandante_nueva_nave(estacion)
    print("Naves de comandante2 después:", len(comandante2.get_naves_asignadas()))

    print("\n--- PRUEBAS DE ADQUISICIÓN CORRECTA ---")
    try:
        comandante2.adquirir_repuesto("Motor", almacen1, "Base Endor")
    except NaveNoComandada as e:
        print(e)
    except RepuestoDeOtraNave as e:
        print(e)
    except RepuestoNoEncontrado as e:
        print(e)
    except RepuestoSinStock as e:
        print(e)

    print("\n--- PRUEBAS DE ERROR ---")

    print("\n-- Caso 1: nave no comandada --")
    try:
        comandante1.adquirir_repuesto("Laser", almacen1, "TIE Avanzado")
    except NaveNoComandada as e:
        print(e)
    except RepuestoDeOtraNave as e:
        print(e)
    except RepuestoNoEncontrado as e:
        print(e)
    except RepuestoSinStock as e:
        print(e)

    print("\n-- Caso 2: repuesto no válido para la nave --")
    try:
        comandante2.adquirir_repuesto("Hyperdrive", almacen2, "TIE Avanzado")
    except NaveNoComandada as e:
        print(e)
    except RepuestoDeOtraNave as e:
        print(e)
    except RepuestoNoEncontrado as e:
        print(e)
    except RepuestoSinStock as e:
        print(e)

    print("\n-- Caso 3: repuesto sin stock --")
    try:
        comandante2.adquirir_repuesto("Escudo", almacen1, "Base Endor")
    except NaveNoComandada as e:
        print(e)
    except RepuestoDeOtraNave as e:
        print(e)
    except RepuestoNoEncontrado as e:
        print(e)
    except RepuestoSinStock as e:
        print(e)

    print("\n-- Caso 4: repuesto no encontrado en almacén --")
    try:
        comandante2.adquirir_repuesto("Bateria", almacen1, "Base Endor")
    except NaveNoComandada as e:
        print(e)
    except RepuestoDeOtraNave as e:
        print(e)
    except RepuestoNoEncontrado as e:
        print(e)
    except RepuestoSinStock as e:
        print(e)


