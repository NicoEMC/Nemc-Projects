import tkinter as tk
from utils.funciones import *

"""
Temporizador con funciones de iniciar, pausar y reiniciar.

Este programa crea una interfaz gráfica de usuario (GUI) para un temporizador utilizando la biblioteca `tkinter`.
Permite a los usuarios configurar un tiempo en minutos (incluyendo valores decimales), iniciar el temporizador,
pausarlo y reiniciarlo.

Características:
- Configuración del tiempo en minutos (soporta decimales).
- Inicio del temporizador y actualización del tiempo restante.
- Pausar el temporizador manteniendo el tiempo restante.
- Reiniciar el temporizador a 00:00.

Funciones principales:
----------------------

1. start_timer():
    Inicia o reanuda el temporizador desde el tiempo restante.
    Si no hay tiempo restante configurado, toma el valor ingresado por el usuario.
    El temporizador muestra minutos y segundos actualizados cada segundo.

2. pause_timer():
    Pausa el temporizador deteniendo la cuenta regresiva y manteniendo el tiempo restante.

3. reset_timer():
    Reinicia el temporizador, restableciendo el tiempo restante a 00:00 y actualizando la pantalla.

"""

# Configuración de la ventana principal
root = tk.Tk()
root.title("Temporizador")

# Variables globales (vinculadas al temporizador)
entry = None
timer_display = None

# Crear la interfaz gráfica
def crear_interfaz():
    global entry, timer_display

    # Título
    title_label = tk.Label(root, text="Temporizador", font=("Helvetica", 24))
    title_label.pack(pady=10)

    # Pantalla del temporizador
    timer_display = tk.Label(root, text="00:00", font=("Helvetica", 48))
    timer_display.pack(pady=10)

    # Campo de entrada
    entry_label = tk.Label(root, text="Tiempo (en minutos, decimales permitidos):", font=("Helvetica", 14))
    entry_label.pack(pady=5)

    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.pack(pady=5)

    # Botones
    start_button = tk.Button(root, text="Iniciar/Reanudar", font=("Helvetica", 14), command=lambda: start_timer(entry, timer_display, root))
    start_button.pack(pady=10)

    pause_button = tk.Button(root, text="Pausar", font=("Helvetica", 14), command=pause_timer)
    pause_button.pack(pady=10)

    reset_button = tk.Button(root, text="Reiniciar", font=("Helvetica", 14), command=lambda: reset_timer(timer_display))
    reset_button.pack(pady=10)

# Crear la interfaz y ejecutar la ventana
crear_interfaz()
root.mainloop()