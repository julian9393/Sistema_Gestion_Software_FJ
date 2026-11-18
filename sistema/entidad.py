
from abc import ABC, abstractmethod
from uuid import uuid4


class Entidad(ABC):
    """Clase abstracta que representa una entidad del sistema."""

    def __init__(self):
        self._id = str(uuid4())

    @property
    def id(self):
        return self._id

    @abstractmethod
    def validar(self):
        """Valida la informacion de la entidad."""
        pass

    @abstractmethod
    def obtener_descripcion(self):
        """Devuelve una descripcion de la entidad."""
        pass