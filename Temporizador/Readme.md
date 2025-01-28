# Temporizador con Tkinter

Este proyecto es una aplicación de temporizador sencilla construida en Python utilizando la biblioteca `tkinter`. Permite configurar un tiempo en minutos (incluyendo decimales), iniciar el temporizador, pausarlo y reiniciarlo. 

## Características

- Configuración del tiempo en minutos, con soporte para valores decimales (por ejemplo, `1.5` para 1 minuto y 30 segundos).
- Inicio del temporizador y actualización en tiempo real del tiempo restante.
- Función para pausar el temporizador.
- Función para reiniciar el temporizador, restableciendo el tiempo a 00:00.

## Requisitos

- Python 3.x
- Biblioteca estándar `tkinter` (incluida en Python).

### Estructura del Proyecto

    proyecto_temporizador/
    │
    ├── temporizador.py
    ├── utils/
    │   └── funciones.py



Cómo usar:
----------
1. Ejecuta el script para abrir la ventana del temporizador.
2. Ingresa el tiempo deseado en minutos en el campo de texto. Por ejemplo:
    - `1.5` para 1 minuto y 30 segundos.
    - `2` para 2 minutos exactos.
3. Presiona el botón **Iniciar/Reanudar** para comenzar la cuenta regresiva.
4. Si deseas pausar el temporizador, presiona el botón **Pausar**.
5. Para reiniciar el temporizador a 00:00, presiona el botón **Reiniciar**.

Elementos de la interfaz gráfica:
---------------------------------
- Etiqueta "Temporizador": Título principal de la ventana.
- Display de tiempo: Muestra el tiempo restante en formato `MM:SS`.
- Campo de texto: Permite al usuario ingresar el tiempo en minutos.
- Botón "Iniciar/Reanudar": Inicia o reanuda la cuenta regresiva.
- Botón "Pausar": Pausa el temporizador.
- Botón "Reiniciar": Reinicia el temporizador a 00:00.

Variables globales:
-------------------
- is_paused: Indica si el temporizador está pausado (True) o corriendo (False).
- remaining_seconds: Almacena el tiempo restante en segundos.

Excepciones:
------------
- Muestra un cuadro de error si el usuario ingresa un valor no numérico o vacío en el campo de texto.

Notas adicionales:
------------------
- Puedes personalizar la fuente, el tamaño de la ventana y los colores según sea necesario.
- Es ideal para realizar tareas que requieren lapsos específicos de tiempo.