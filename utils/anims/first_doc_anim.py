import time

from ..clear_console import clear_console
from .loading_anim import startAnim,stopAnim

def first_doc_anim():
    clear_console()
    print("Vamos a empezar creando tu primer documento! :)")
    spinner = startAnim("Espera por favor")
    time.sleep(5)
    stopAnim(spinner)
