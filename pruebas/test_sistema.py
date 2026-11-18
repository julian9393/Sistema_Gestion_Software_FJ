
import unittest

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


class PruebasIntegralesSistema(unittest.TestCase):
    """Pruebas integrales de los modulos de Software FJ."""

    def setUp(self):
        """Prepara los datos necesarios para cada prueba."""

        self.cliente = Cliente(
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )

        self.sala = ServicioSala(
            "Sala de reuniones",
            50000,
            20
        )

        self.equipo = AlquilerEquipo(
            "Computador portatil",
            12000,
            5
        )

        self.asesoria = Asesoria(
            "Consultoria tecnologica",
            80000,
            "Desarrollo de software"
        )

    def test_01_creacion_cliente(self):
        self.assertEqual(self.cliente.nombre, "Carlos Perez")
        self.assertTrue(self.cliente.validar())

    def test_02_correo_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente(
                "Carlos Perez",
                "correo_invalido",
                "3001234567"
            )

    def test_03_tarifa_decimal_rechazada(self):
        with self.assertRaises(DatosInvalidosError):
            ServicioSala(
                "Sala de reuniones",
                50000.5,
                20
            )

    def test_04_calculo_costo_sala(self):
        total = self.sala.calcular_costo(3)

        self.assertEqual(total, 150000)
        self.assertIsInstance(total, int)

    def test_05_calculo_costo_equipos(self):
        total = self.equipo.calcular_costo(
            4,
            cantidad=2
        )

        self.assertEqual(total, 96000)
        self.assertIsInstance(total, int)

    def test_06_calculo_costo_asesoria(self):
        total = self.asesoria.calcular_costo(
            2,
            descuento=10,
            impuesto=19
        )

        self.assertEqual(total, 171360)
        self.assertIsInstance(total, int)

    def test_07_confirmacion_reserva(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            3
        )

        reserva.confirmar()

        self.assertEqual(reserva.estado, "Confirmada")
        self.assertEqual(reserva.total, 150000)

    def test_08_finalizacion_reserva(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2
        )

        reserva.confirmar()
        reserva.finalizar()

        self.assertEqual(reserva.estado, "Finalizada")

    def test_09_cancelacion_reserva(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2
        )

        reserva.cancelar()

        self.assertEqual(reserva.estado, "Cancelada")

    def test_10_confirmacion_reserva_cancelada(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2
        )

        reserva.cancelar()

        with self.assertRaises(ReservaError):
            reserva.confirmar()

    def test_11_duracion_invalida(self):
        with self.assertRaises(DatosInvalidosError):
            Reserva(
                self.cliente,
                self.sala,
                -2
            )

    def test_12_equipo_no_disponible(self):
        equipo_agotado = AlquilerEquipo(
            "Proyector",
            25000,
            0
        )

        reserva = Reserva(
            self.cliente,
            equipo_agotado,
            2
        )

        with self.assertRaises(ServicioNoDisponibleError):
            reserva.confirmar()


if __name__ == "__main__":
    unittest.main(verbosity=2)
