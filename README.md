# Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Proyecto académico – Fase 4: Prácticas simuladas**  
**Empresa simulada:** Software FJ  
**Asignatura:** Programación  
**Universidad Nacional Abierta y a Distancia (UNAD)**

## 1. Descripción del proyecto

El proyecto consiste en desarrollar un sistema orientado a objetos para gestionar clientes, servicios y reservas de la empresa simulada Software FJ.

La aplicación permite registrar clientes, administrar diferentes tipos de servicios y gestionar reservas mediante validaciones, control de estados y manejo de excepciones.

Se implementan mecanismos de registro de eventos y errores mediante archivos de log, con el propósito de facilitar el seguimiento de las operaciones y mejorar la estabilidad del sistema.

## 2. Objetivo general

Desarrollar una aplicación basada en programación orientada a objetos que permita gestionar clientes, servicios y reservas, incorporando mecanismos de manejo de excepciones y registro de eventos para garantizar un funcionamiento controlado y confiable.

## 3. Funcionalidades principales

- Registro y validación de clientes.
- Administración de servicios.
- Gestión de servicios de reserva de salas.
- Gestión de alquiler de equipos.
- Gestión de asesorías especializadas.
- Creación, confirmación, cancelación y finalización de reservas.
- Validación de datos y disponibilidad de servicios.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en archivos de log.
- Pruebas automatizadas para verificar el funcionamiento del sistema.

## 4. Estructura del proyecto

```text
Sistema_Gestion_Software_FJ/
│
├── main.py
├── README.md
├── .gitignore
│
├── sistema/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── servicio_sala.py
│   ├── alquiler_equipo.py
│   ├── asesoria.py
│   ├── reserva.py
│   ├── excepciones.py
│   └── gestor_logs.py
│
├── pruebas/
│   ├── test_sistema.py
│   ├── test_logs.py
│   └── test_excepciones.py
│
├── logs/
│   ├── eventos.log
│   └── errores.log
│
└── evidencia/
    └── Capturas de las pruebas y resultados
```

## 5. Tecnologías utilizadas

- Python 3.14.
- Programación orientada a objetos.
- Manejo de excepciones.
- Módulo `logging` para el registro de eventos y errores.
- Módulo `unittest` para las pruebas automatizadas.
- Git y GitHub para el control de versiones.
- Visual Studio Code como entorno de desarrollo.

## 6. Manejo de excepciones

El sistema incorpora excepciones personalizadas para controlar situaciones como:

- Datos ingresados con formatos incorrectos.
- Registro de entidades duplicadas.
- Errores relacionados con las reservas.
- Servicios que no se encuentran disponibles.

También se utilizan estructuras `try`, `except`, `else` y `finally`, junto con el encadenamiento de excepciones para conservar información sobre el error original.

## 7. Registro de eventos y errores

La aplicación utiliza archivos de registro para almacenar información sobre las operaciones realizadas.

- `eventos.log`: registra las operaciones y acontecimientos relevantes del sistema.
- `errores.log`: almacena los errores que se presentan durante la ejecución.

Estos registros permiten realizar seguimiento y facilitar la identificación de situaciones que requieren revisión.

## 8. Ejecución del proyecto

Para ejecutar la aplicación, se debe abrir una terminal en la carpeta principal del proyecto y ejecutar:

```powershell
python main.py
```

Si el comando `python` no está disponible en Windows, se puede utilizar la ruta del ejecutable de Python instalado en el equipo.

## 9. Ejecución de las pruebas

Para ejecutar las pruebas integrales:

```powershell
python -m unittest pruebas.test_sistema -v
```

Para ejecutar las pruebas de registro de eventos:

```powershell
python -m pruebas.test_logs
```

Para ejecutar las pruebas de excepciones:

```powershell
python -m pruebas.test_excepciones
```

Las pruebas permiten verificar las validaciones, los cálculos, los estados de las reservas, la disponibilidad de los servicios y el comportamiento del manejo de excepciones.

## 10. Repositorio del proyecto

El código fuente y los archivos del proyecto se encuentran disponibles en el siguiente repositorio:

[GitHub - Sistema_Gestion_Software_FJ](https://github.com/julian9393/Sistema_Gestion_Software_FJ.git)

## 11. Consideraciones finales

El desarrollo permite aplicar los fundamentos de programación orientada a objetos, la reutilización de código, el polimorfismo, las excepciones personalizadas y el registro de eventos.

Las pruebas realizadas permiten comprobar el funcionamiento de los componentes implementados y contribuyen a la confiabilidad del sistema.