
from sistema.servicio import Servicio
from sistema.excepciones import DatosInvalidosError


class Asesoria(Servicio):
    """Representa un servicio de asesoria especializada."""

    def __init__(
        self,
        nombre,
        tarifa_hora,
        especialidad,
        disponible=True
    ):
        super().__init__(nombre, tarifa_hora, disponible)

        self._especialidad = (
            especialidad.strip()
            if isinstance(especialidad, str)
            else especialidad
        )

        self.validar()

    @property
    def especialidad(self):
        return self._especialidad

    def validar(self):
        super().validar()

        if (
            not isinstance(self._especialidad, str)
            or not self._especialidad
        ):
            raise DatosInvalidosError(
                "La especialidad de la asesoria es obligatoria."
            )

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if not self._disponible:
            raise DatosInvalidosError(
                "La asesoria no se encuentra disponible."
            )

        return self._calcular_total(
            duracion,
            descuento=descuento,
            impuesto=impuesto
        )

    def obtener_descripcion(self):
        return (
            f"{super().obtener_descripcion()} | "
            f"Especialidad: {self._especialidad}"
        )
