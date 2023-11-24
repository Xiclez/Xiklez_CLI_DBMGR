import os

def clear_console():
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para Mac y Linux (os.name: 'posix')
    else:
        _ = os.system('clear')
