
import re

from sistema.entidad import Entidad
from sistema.excepciones import DatosInvalidosError


class Cliente(Entidad):
    """Representa un cliente registrado en el sistema."""

    def __init__(self, nombre, correo, telefono):
        super().__init__()

        self._nombre = nombre.strip() if isinstance(nombre, str) else nombre
        self._correo = correo.strip().lower() if isinstance(correo, str) else correo
        self._telefono = telefono.strip() if isinstance(telefono, str) else telefono

        self.validar()

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def validar(self):
        """Comprueba que los datos del cliente sean correctos."""

        if not isinstance(self._nombre, str) or len(self._nombre) < 3:
            raise DatosInvalidosError(
                "El nombre debe contener al menos tres caracteres."
            )

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", self._correo):
            raise DatosInvalidosError(
                "El correo electronico no tiene un formato valido."
            )

        if not isinstance(self._telefono, str) or not self._telefono.isdigit():
            raise DatosInvalidosError(
                "El telefono debe contener solamente numeros."
            )

        if len(self._telefono) < 7 or len(self._telefono) > 15:
            raise DatosInvalidosError(
                "El telefono debe tener entre 7 y 15 digitos."
            )

        return True

    def obtener_descripcion(self):
        return (
            f"Cliente: {self._nombre} | "
            f"Correo: {self._correo} | "
            f"Telefono: {self._telefono}"
        )

    def __str__(self):
        return self.obtener_descripcion()