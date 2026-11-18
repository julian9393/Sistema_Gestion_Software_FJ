
from sistema.cliente import Cliente
from sistema.servicio_sala import ServicioSala
from sistema.alquiler_equipo import AlquilerEquipo
from sistema.asesoria import Asesoria
from sistema.reserva import Reserva

from sistema.excepciones import (
    DatosInvalidosError,
    ReservaError,
    ServicioNoDisponibleError
)


def ejecutar_pruebas():
    print("======================================")
    print(" PRUEBAS DEL BLOQUE 3 - RESERVAS")
    print("======================================")

    cliente = Cliente(
        "Carlos Perez",
        "carlos@gmail.com",
        "3001234567"
    )

    sala = ServicioSala(
        "Sala de reuniones",
        50000,
        20
    )

    equipo = AlquilerEquipo(
        "Computador portatil",
        12000,
        5
    )

    asesoria = Asesoria(
        "Consultoria tecnologica",
        80000,
        "Desarrollo de software"
    )

    # PRUEBA 1: Crear una reserva de sala
    print("\n1. CREACION DE RESERVA")

    reserva_sala = Reserva(
        cliente,
        sala,
        3
    )

    print(reserva_sala.obtener_descripcion())

    # PRUEBA 2: Confirmar reserva
    print("\n2. CONFIRMACION DE RESERVA")

    print(reserva_sala.confirmar())
    print("Estado:", reserva_sala.estado)
    print("Total:", reserva_sala.total)

    # PRUEBA 3: Finalizar reserva
    print("\n3. FINALIZACION DE RESERVA")

    print(reserva_sala.finalizar())
    print("Estado:", reserva_sala.estado)

    # PRUEBA 4: Reserva de equipos
    print("\n4. RESERVA DE EQUIPOS")

    reserva_equipo = Reserva(
        cliente,
        equipo,
        4,
        cantidad=2
    )

    print(reserva_equipo.confirmar())
    print("Total:", reserva_equipo.total)

    # PRUEBA 5: Reserva de asesoria
    print("\n5. RESERVA DE ASESORIA")

    reserva_asesoria = Reserva(
        cliente,
        asesoria,
        2,
        descuento=10,
        impuesto=19
    )

    print(reserva_asesoria.confirmar())
    print("Total:", reserva_asesoria.total)

    # PRUEBA 6: Cancelar reserva
    print("\n6. CANCELACION DE RESERVA")

    reserva_cancelada = Reserva(
        cliente,
        sala,
        2
    )

    print(reserva_cancelada.cancelar())
    print("Estado:", reserva_cancelada.estado)

    # PRUEBA 7: Intentar confirmar una reserva cancelada
    print("\n7. CONTROL DE ESTADOS")

    try:
        reserva_cancelada.confirmar()

    except ReservaError as error:
        print("Error controlado correctamente:", error)

    # PRUEBA 8: Validacion de duracion incorrecta
    print("\n8. VALIDACION DE DURACION")

    try:
        Reserva(
            cliente,
            sala,
            -3
        )

    except DatosInvalidosError as error:
        print("Error controlado correctamente:", error)

    # PRUEBA 9: Servicio no disponible
        print("\n9. SERVICIO NO DISPONIBLE")

    try:
        equipo_agotado = AlquilerEquipo("Proyector", 25000, 0)
        reserva_agotada = Reserva(cliente, equipo_agotado, 2)
        reserva_agotada.confirmar()

    except ServicioNoDisponibleError as error:
        print(f"Error controlado correctamente: {error}")

    # PRUEBA 10: Comprobar precios enteros
    print("\n10. COMPROBACION DE PRECIOS ENTEROS")

    print("Total de sala:", reserva_sala.total)
    print("Tipo de dato:", type(reserva_sala.total).__name__)

    print("Total de equipos:", reserva_equipo.total)
    print("Tipo de dato:", type(reserva_equipo.total).__name__)

    print("Total de asesoria:", reserva_asesoria.total)
    print("Tipo de dato:", type(reserva_asesoria.total).__name__)

    print("\n======================================")
    print(" FINALIZACION DE LAS PRUEBAS")
    print("======================================")


if __name__ == "__main__":
    ejecutar_pruebas()
