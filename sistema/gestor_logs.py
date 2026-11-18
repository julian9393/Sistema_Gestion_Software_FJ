
import logging
from pathlib import Path


class GestorLogs:
    """Administra el registro de eventos y errores del sistema Software FJ."""

    def __init__(self, nombre="SoftwareFJ"):
        # Crear la carpeta logs en la raiz del proyecto.
        ruta_proyecto = Path(__file__).resolve().parent.parent
        self.ruta_logs = ruta_proyecto / "logs"
        self.ruta_logs.mkdir(parents=True, exist_ok=True)

        # Crear el registrador principal.
        self.logger = logging.getLogger(nombre)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # Evitar que se agreguen manejadores duplicados.
        if not self.logger.handlers:
            formato = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            # Archivo para registrar los eventos del sistema.
            archivo_eventos = logging.FileHandler(
                self.ruta_logs / "eventos.log",
                encoding="utf-8"
            )
            archivo_eventos.setLevel(logging.INFO)
            archivo_eventos.setFormatter(formato)

            # Archivo exclusivo para registrar errores.
            archivo_errores = logging.FileHandler(
                self.ruta_logs / "errores.log",
                encoding="utf-8"
            )
            archivo_errores.setLevel(logging.ERROR)
            archivo_errores.setFormatter(formato)

            self.logger.addHandler(archivo_eventos)
            self.logger.addHandler(archivo_errores)

    def registrar_evento(self, mensaje):
        """Registra una actividad normal del sistema."""
        self.logger.info(mensaje)

    def registrar_advertencia(self, mensaje):
        """Registra una situacion que requiere atencion."""
        self.logger.warning(mensaje)

    def registrar_error(self, mensaje, error=None):
        """Registra un error y su informacion tecnica cuando existe."""
        if error is not None and error.__traceback__ is not None:
            informacion_error = (
                type(error),
                error,
                error.__traceback__
            )
            self.logger.error(
                "%s | %s: %s",
                mensaje,
                type(error).__name__,
                error,
                exc_info=informacion_error
            )
        elif error is not None:
            self.logger.error(
                "%s | %s: %s",
                mensaje,
                type(error).__name__,
                error
            )
        else:
            self.logger.error(mensaje)
