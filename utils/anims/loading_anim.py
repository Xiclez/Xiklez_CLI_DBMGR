import sys
import time
import threading

# Variable para controlar el estado de la animación
is_spinning = True

def spinner_animation(message="Espera por favor..."):
    global is_spinning
    spinner = threading.Thread(target=_spinner, args=(message,), daemon=True)
    return spinner

def _spinner(message):
    global is_spinning
    spinner = "|/-\\"
    idx = 0
    while is_spinning:
        sys.stdout.write("\r" + message + " " + spinner[idx % len(spinner)])
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\r")  # Limpiar la línea cuando se detenga la animación
    sys.stdout.flush()

def startAnim(message="Espera por favor..."):
    global is_spinning
    is_spinning = True  # Habilitar la animación
    spinner = spinner_animation(message)
    spinner.start()
    return spinner

def stopAnim(spinner):
    global is_spinning
    is_spinning = False  # Indicar al hilo que debe detenerse
    spinner.join()  # Esperar a que el hilo termine
