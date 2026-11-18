
from sistema.gestor_logs import GestorLogs
from sistema.excepciones import DatosInvalidosError


def ejecutar_prueba_logs():
    gestor = GestorLogs()

    print("======================================")
    print(" PRUEBAS DEL BLOQUE 4 - REGISTRO LOGS")
    print("======================================")

    # PRUEBA 1: Registro de inicio del sistema.
    print("\n1. REGISTRO DE EVENTO")

    gestor.registrar_evento(
        "Inicio de las pruebas del sistema Software FJ."
    )

    print("Evento registrado correctamente.")

    # PRUEBA 2: Manejo de try, except, else y finally.
    print("\n2. MANEJO DE EXCEPCIONES")

    try:
        resultado = 100 + 50

    except Exception as error:
        gestor.registrar_error(
            "Se produjo un error durante la operacion.",
            error
        )
        print(f"Error controlado: {error}")

    else:
        gestor.registrar_evento(
            f"Operacion realizada correctamente. Resultado: {resultado}"
        )
        print(f"Operacion correcta. Resultado: {resultado}")

    finally:
        gestor.registrar_evento(
            "Finalizacion del bloque de manejo de excepciones."
        )
        print("Bloque finally ejecutado correctamente.")

    # PRUEBA 3: Registro de una advertencia.
    print("\n3. REGISTRO DE ADVERTENCIA")

    gestor.registrar_advertencia(
        "Advertencia de prueba del sistema Software FJ."
    )

    print("Advertencia registrada correctamente.")

    # PRUEBA 4: Captura y registro de un error.
    print("\n4. REGISTRO DE ERROR")

    try:
        raise DatosInvalidosError(
            "Dato de prueba no valido."
        )

    except DatosInvalidosError as error:
        gestor.registrar_error(
            "Se capturo una excepcion personalizada.",
            error
        )

        print(f"Error controlado correctamente: {error}")

    # PRUEBA 5: Registro de finalizacion.
    gestor.registrar_evento(
        "Finalizacion de las pruebas del bloque 4."
    )

    print("\n5. FINALIZACION DEL REGISTRO")
    print("Los registros fueron enviados a los archivos LOG.")

    print("\n======================================")
    print(" FINALIZACION DE LAS PRUEBAS")
    print("======================================")


if __name__ == "__main__":
    ejecutar_prueba_logs()
