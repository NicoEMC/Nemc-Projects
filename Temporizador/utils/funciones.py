import time
from tkinter import messagebox

# Variables globales necesarias
is_paused = False
remaining_seconds = 0

def start_timer(entry, timer_display, root):
    """
    Inicia o reanuda el temporizador desde el tiempo restante.
    Si no hay tiempo restante, lo toma del campo de entrada.
    """
    global is_paused, remaining_seconds

    try:
        if remaining_seconds == 0:  # Si no hay tiempo restante, lo toma del campo de entrada
            remaining_seconds = float(entry.get()) * 60

        is_paused = False
        while remaining_seconds > 0:
            if is_paused:  # Si el temporizador está pausado, salir del ciclo
                break

            mins, secs = divmod(int(remaining_seconds), 60)
            timer_display.config(text=f"{mins:02d}:{secs:02d}")
            root.update()
            time.sleep(1)
            remaining_seconds -= 1

        if remaining_seconds <= 0:
            timer_display.config(text="00:00")
            messagebox.showinfo("Timer", "¡El tiempo ha terminado!")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido (por ejemplo, 1.5 para 1 minuto y 30 segundos).")


def pause_timer():
    """
    Pausa el temporizador, deteniendo la cuenta regresiva pero manteniendo el tiempo restante.
    """
    global is_paused
    is_paused = True


def reset_timer(timer_display):
    """
    Reinicia el temporizador, estableciendo el tiempo restante a 00:00 y actualizando la pantalla.
    """
    global is_paused, remaining_seconds
    is_paused = True  # Detener el temporizador si está corriendo
    remaining_seconds = 0  # Reiniciar el tiempo restante
    timer_display.config(text="00:00")  # Resetear el display