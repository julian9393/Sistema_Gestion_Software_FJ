
from sistema.servicio import Servicio
from sistema.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class AlquilerEquipo(Servicio):
    """Representa el alquiler de equipos."""

    def __init__(
        self,
        nombre,
        tarifa_hora,
        cantidad_disponible,
        disponible=True
    ):
        super().__init__(nombre, tarifa_hora, disponible)

        self._cantidad_disponible = cantidad_disponible

        self.validar()

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    def validar(self):
        super().validar()

        if (
            isinstance(self._cantidad_disponible, bool)
            or not isinstance(self._cantidad_disponible, int)
            or self._cantidad_disponible < 0
        ):
            raise DatosInvalidosError(
                "La cantidad disponible debe ser un entero no negativo."
            )

        return True

    def calcular_costo(
        self,
        duracion,
        cantidad=1,
        descuento=0,
        impuesto=0
    ):
        if not self._disponible or self._cantidad_disponible == 0:
            raise ServicioNoDisponibleError(
                "El equipo no se encuentra disponible."
            )

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise DatosInvalidosError(
                "La cantidad solicitada debe ser un entero positivo."
            )

        if cantidad > self._cantidad_disponible:
            raise ServicioNoDisponibleError(
                "No hay suficientes unidades disponibles."
            )

        return self._calcular_total(
            duracion,
            cantidad=cantidad,
            descuento=descuento,
            impuesto=impuesto
        )

    def obtener_descripcion(self):
        return (
            f"{super().obtener_descripcion()} | "
            f"Unidades disponibles: {self._cantidad_disponible}"
        )
