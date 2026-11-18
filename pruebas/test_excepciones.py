
from sistema.gestor_logs import GestorLogs
from sistema.excepciones import (
    ErrorSistema,
    DatosInvalidosError
)


gestor = GestorLogs()


def convertir_tarifa(valor):
    """Convierte una tarifa y controla los errores de conversion."""

    try:
        tarifa = int(valor)

        if tarifa <= 0:
            raise ValueError("La tarifa debe ser mayor que cero.")

        return tarifa

    except (ValueError, TypeError) as error:
        raise DatosInvalidosError(
            "No fue posible convertir la tarifa a un entero positivo."
        ) from error


def ejecutar_pruebas():
    print("======================================")
    print(" PRUEBAS DE EXCEPCIONES ENCADENADAS")
    print("======================================")

    # PRUEBA 1: Conversion correcta.
    print("\n1. CONVERSION DE TARIFA")

    try:
        tarifa = convertir_tarifa("50000")
        gestor.registrar_evento(
            f"Tarifa convertida correctamente: ${tarifa}"
        )
        print(f"Tarifa convertida correctamente: ${tarifa}")

    except DatosInvalidosError as error:
        gestor.registrar_error("Error al convertir tarifa.", error)
        print(f"Error controlado: {error}")

    # PRUEBA 2: Control de una tarifa invalida.
    print("\n2. CONTROL DE TARIFA INVALIDA")

    try:
        convertir_tarifa("abc")

    except DatosInvalidosError as error:
        gestor.registrar_error(
            "Se detecto una tarifa con formato incorrecto.",
            error
        )

        print(f"Error controlado correctamente: {error}")

        if error.__cause__ is not None:
            print(
                "Causa original:",
                type(error.__cause__).__name__,
                "-",
                error.__cause__
            )

    # PRUEBA 3: Control de una tarifa negativa.
    print("\n3. CONTROL DE TARIFA NEGATIVA")

    try:
        convertir_tarifa("-1000")

    except DatosInvalidosError as error:
        gestor.registrar_error(
            "Se detecto una tarifa negativa.",
            error
        )
        print(f"Error controlado correctamente: {error}")

        if error.__cause__ is not None:
            print(
                "Causa original:",
                type(error.__cause__).__name__,
                "-",
                error.__cause__
            )

    # PRUEBA 4: Comprobacion del encadenamiento.
    print("\n4. COMPROBACION DE EXCEPCIONES ENCADENADAS")

    try:
        convertir_tarifa("texto incorrecto")

    except ErrorSistema as error:
        if error.__cause__ is not None:
            print("Encadenamiento de excepciones comprobado.")
            print("La causa original se conserva correctamente.")
        else:
            print("No se encontro la causa original.")

    print("\n======================================")
    print(" FINALIZACION DE LAS PRUEBAS")
    print("======================================")


if __name__ == "__main__":
    ejecutar_pruebas()
