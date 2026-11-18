
from sistema.servicio import Servicio
from sistema.excepciones import DatosInvalidosError


class ServicioSala(Servicio):
    """Representa el servicio de reserva de salas."""

    def __init__(
        self,
        nombre,
        tarifa_hora,
        capacidad,
        disponible=True
    ):
        super().__init__(nombre, tarifa_hora, disponible)

        self._capacidad = capacidad

        self.validar()

    @property
    def capacidad(self):
        return self._capacidad

    def validar(self):
        super().validar()

        if (
            isinstance(self._capacidad, bool)
            or not isinstance(self._capacidad, int)
            or self._capacidad <= 0
        ):
            raise DatosInvalidosError(
                "La capacidad de la sala debe ser un entero positivo."
            )

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if not self._disponible:
            raise DatosInvalidosError(
                "La sala no se encuentra disponible."
            )

        return self._calcular_total(
            duracion,
            descuento=descuento,
            impuesto=impuesto
        )

    def obtener_descripcion(self):
        return (
            f"{super().obtener_descripcion()} | "
            f"Capacidad: {self._capacidad} personas"
        )
