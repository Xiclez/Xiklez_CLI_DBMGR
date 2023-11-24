#Create
from utils.clear_console import clear_console
from utils.ascii_arts import draw_create

def insert_document(collection, schema):
    clear_console()
    print(draw_create())
    if schema == "1":  
        titulo = input("Ingrese el título del videojuego: ")
        clasificacion = input("Ingrese la clasificación del videojuego: ")
        genero = input("Ingrese el género del videojuego: ")
        new_document = {"titulo": titulo, "clasificacion": clasificacion, "genero": genero}

    elif schema == "2": 
        nombre_cancion = input("Ingrese el nombre de la canción: ")
        album = input("Ingrese el nombre del álbum: ")
        genero_musical = input("Ingrese el género musical: ")
        new_document = {"nombre_cancion": nombre_cancion, "album": album, "genero_musical": genero_musical}

    elif schema == "3":  
        nombre_peli = input("Ingrese el nombre de la película: ")
        director = input("Ingrese el nombre del director: ")
        genero_pelicula = input("Ingrese el género de la película: ")
        new_document = {"nombre_peli": nombre_peli, "director": director, "genero_pelicula": genero_pelicula}

    else:  
        curp = input("Ingrese el CURP: ")
        calificacion = float(input("Ingrese la calificación: "))
        materia = input("Ingrese la materia: ")
        new_document = {"CURP": curp, "calificacion": calificacion, "materia": materia}

    collection.insert_one(new_document)
    print("Documento insertado exitosamente.")
    clear_console()
