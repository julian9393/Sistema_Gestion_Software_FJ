
class ErrorSistema(Exception):
    """Excepcion base para los errores del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se utiliza cuando los datos ingresados no son validos."""
    pass


class EntidadDuplicadaError(ErrorSistema):
    """Se utiliza cuando una entidad ya se encuentra registrada."""
    pass


class ReservaError(ErrorSistema):
    """Se utiliza cuando ocurre un problema con una reserva."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se utiliza cuando un servicio no esta disponible."""
    pass