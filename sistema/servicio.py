
from abc import abstractmethod

from sistema.entidad import Entidad
from sistema.excepciones import DatosInvalidosError


class Servicio(Entidad):
    """Clase abstracta que representa un servicio de Software FJ."""

    def __init__(self, nombre, tarifa_base, disponible=True):
        super().__init__()

        self._nombre = nombre.strip() if isinstance(nombre, str) else nombre
        self._tarifa_base = tarifa_base
        self._disponible = disponible

        self._validar_datos_base()

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def disponible(self):
        return self._disponible

    def _validar_datos_base(self):
        if not isinstance(self._nombre, str) or not self._nombre:
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if (
            isinstance(self._tarifa_base, bool)
            or not isinstance(self._tarifa_base, int)
            or self._tarifa_base <= 0
        ):
            raise DatosInvalidosError(
                "La tarifa del servicio debe ser un numero entero positivo."
            )

        if not isinstance(self._disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

    def validar(self):
        """Valida los datos generales del servicio."""
        self._validar_datos_base()
        return True

    def obtener_descripcion(self):
        estado = "Disponible" if self._disponible else "No disponible"

        return (
            f"Servicio: {self._nombre} | "
            f"Tarifa base: ${self._tarifa_base} | "
            f"Estado: {estado}"
        )

    def _calcular_total(
        self,
        duracion,
        cantidad=1,
        descuento=0,
        impuesto=0
    ):
        """Calcula el costo utilizando exclusivamente valores enteros."""

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, int)
            or duracion <= 0
        ):
            raise DatosInvalidosError(
                "La duracion debe ser un numero entero positivo."
            )

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):
            raise DatosInvalidosError(
                "La cantidad debe ser un numero entero positivo."
            )

        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, int)
            or not 0 <= descuento <= 100
        ):
            raise DatosInvalidosError(
                "El descuento debe ser un numero entero entre 0 y 100."
            )

        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, int)
            or not 0 <= impuesto <= 100
        ):
            raise DatosInvalidosError(
                "El impuesto debe ser un numero entero entre 0 y 100."
            )

        subtotal = self._tarifa_base * duracion * cantidad

        valor_descuento = subtotal * descuento / 100
        subtotal_con_descuento = subtotal - valor_descuento

        valor_impuesto = subtotal_con_descuento * impuesto / 100

        total = subtotal_con_descuento + valor_impuesto

        return int(round(total))

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Cada servicio implementa su propio calculo de costo."""
        pass
