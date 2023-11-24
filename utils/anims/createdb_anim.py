import time

from ..clear_console import clear_console
from .loading_anim import startAnim,stopAnim
from ..ascii_arts import draw_sucess,draw_wait 

def createdb_anim():
    clear_console()
    print(draw_wait())
    spinner = startAnim("Creando base de datos")
    time.sleep(2)
    stopAnim(spinner)
    print(draw_sucess())
    time.sleep(1)
    clear_console()

