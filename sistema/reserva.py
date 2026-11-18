
from sistema.entidad import Entidad
from sistema.cliente import Cliente
from sistema.servicio import Servicio
from sistema.alquiler_equipo import AlquilerEquipo
from sistema.excepciones import (
    DatosInvalidosError,
    ReservaError,
    ServicioNoDisponibleError
)
from sistema.gestor_logs import GestorLogs


# Gestor de registros para las operaciones de reservas.
gestor_logs = GestorLogs("SoftwareFJ.Reservas")


class Reserva(Entidad):
    """Representa una reserva de un servicio de Software FJ."""

    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Finalizada"
    )

    def __init__(
        self,
        cliente,
        servicio,
        duracion,
        cantidad=1,
        descuento=0,
        impuesto=0
    ):
        super().__init__()

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._cantidad = cantidad
        self._descuento = descuento
        self._impuesto = impuesto
        self._estado = "Pendiente"
        self._total = None

        self.validar()

        gestor_logs.registrar_evento(
            f"Reserva creada. ID: {self.id} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre}"
        )

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def descuento(self):
        return self._descuento

    @property
    def impuesto(self):
        return self._impuesto

    @property
    def estado(self):
        return self._estado

    @property
    def total(self):
        return self._total

    def validar(self):
        """Comprueba que los datos de la reserva sean correctos."""

        if not isinstance(self._cliente, Cliente):
            raise DatosInvalidosError(
                "La reserva debe estar asociada a un cliente valido."
            )

        if not isinstance(self._servicio, Servicio):
            raise DatosInvalidosError(
                "La reserva debe estar asociada a un servicio valido."
            )

        if (
            isinstance(self._duracion, bool)
            or not isinstance(self._duracion, int)
            or self._duracion <= 0
        ):
            raise DatosInvalidosError(
                "La duracion debe ser un numero entero positivo."
            )

        if (
            isinstance(self._cantidad, bool)
            or not isinstance(self._cantidad, int)
            or self._cantidad <= 0
        ):
            raise DatosInvalidosError(
                "La cantidad debe ser un numero entero positivo."
            )

        if (
            isinstance(self._descuento, bool)
            or not isinstance(self._descuento, int)
            or not 0 <= self._descuento <= 100
        ):
            raise DatosInvalidosError(
                "El descuento debe ser un entero entre 0 y 100."
            )

        if (
            isinstance(self._impuesto, bool)
            or not isinstance(self._impuesto, int)
            or not 0 <= self._impuesto <= 100
        ):
            raise DatosInvalidosError(
                "El impuesto debe ser un entero entre 0 y 100."
            )

        if not self._servicio.disponible:
            raise ServicioNoDisponibleError(
                "No se puede reservar un servicio no disponible."
            )

        return True

    def _calcular_costo_reserva(self):
        """Calcula el costo de acuerdo con el tipo de servicio."""

        if isinstance(self._servicio, AlquilerEquipo):
            return self._servicio.calcular_costo(
                self._duracion,
                cantidad=self._cantidad,
                descuento=self._descuento,
                impuesto=self._impuesto
            )

        return self._servicio.calcular_costo(
            self._duracion,
            descuento=self._descuento,
            impuesto=self._impuesto
        )

    def confirmar(self):
        """Confirma una reserva y registra la operación."""

        try:
            if self._estado != "Pendiente":
                raise ReservaError(
                    "Solo se pueden confirmar reservas pendientes."
                )

            self.validar()
            self._total = self._calcular_costo_reserva()
            self._estado = "Confirmada"

            gestor_logs.registrar_evento(
                f"Reserva confirmada. ID: {self.id} | "
                f"Total: ${self._total}"
            )

            return (
                f"Reserva {self.id} confirmada correctamente. "
                f"Total: ${self._total}"
            )

        except Exception as error:
            gestor_logs.registrar_error(
                f"Error al confirmar la reserva {self.id}.",
                error
            )
            raise

    def cancelar(self):
        """Cancela una reserva y registra la operación."""

        try:
            if self._estado not in ("Pendiente", "Confirmada"):
                raise ReservaError(
                    "No se puede cancelar una reserva finalizada o cancelada."
                )

            self._estado = "Cancelada"

            gestor_logs.registrar_evento(
                f"Reserva cancelada. ID: {self.id}"
            )

            return (
                f"Reserva {self.id} cancelada correctamente."
            )

        except Exception as error:
            gestor_logs.registrar_error(
                f"Error al cancelar la reserva {self.id}.",
                error
            )
            raise

    def finalizar(self):
        """Finaliza una reserva y registra la operación."""

        try:
            if self._estado != "Confirmada":
                raise ReservaError(
                    "Solo se pueden finalizar reservas confirmadas."
                )

            self._estado = "Finalizada"

            gestor_logs.registrar_evento(
                f"Reserva finalizada. ID: {self.id}"
            )

            return (
                f"Reserva {self.id} finalizada correctamente."
            )

        except Exception as error:
            gestor_logs.registrar_error(
                f"Error al finalizar la reserva {self.id}.",
                error
            )
            raise

    def obtener_descripcion(self):
        """Devuelve la informacion completa de la reserva."""

        total = (
            f"${self._total}"
            if self._total is not None
            else "Pendiente de calcular"
        )

        return (
            f"Reserva: {self.id}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duracion: {self._duracion} horas\n"
            f"Cantidad: {self._cantidad}\n"
            f"Estado: {self._estado}\n"
            f"Total: {total}"
        )

    def __str__(self):
        return self.obtener_descripcion()
