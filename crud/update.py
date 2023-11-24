#Update
import time 

from .read import search_document
from utils.clear_console import clear_console
from utils.ascii_arts import draw_update

def update_document(collection, schema):
    clear_console()
    print(draw_update())
    documents = search_document(collection, schema, print_results=True)
    if documents is None or len(documents) == 0:
        return
    clear_console()
    # Listar los documentos y pedir al usuario que elija uno para actualizar
    print(draw_update())
    print("\nSeleccione el documento que desea actualizar:")
    for i, doc in enumerate(documents):
        print(f"{i + 1}. {doc}")

    try:
        choice = int(input("\nIngrese el número del documento a actualizar (o 0 para cancelar): "))
        if choice == 0:
            print("Actualización cancelada.")
            return
        elif 1 <= choice <= len(documents):
            document_to_update = documents[choice - 1]
            new_values = {}
            if schema == "1":  # Videojuegos
                new_values["titulo"] = input("Ingrese el nuevo título (deje en blanco para mantener el actual): ")
                new_values["clasificacion"] = input("Ingrese la nueva clasificación (deje en blanco para mantener la actual): ")
                new_values["genero"] = input("Ingrese el nuevo género (deje en blanco para mantener el actual): ")
            elif schema == "2":  # Música
                new_values["nombre_cancion"] = input("Ingrese el nuevo nombre de la canción (deje en blanco para mantener el actual): ")
                new_values["album"] = input("Ingrese el nuevo nombre del álbum (deje en blanco para mantener el actual): ")
                new_values["genero_musical"] = input("Ingrese el nuevo género musical (deje en blanco para mantener el actual): ")
            elif schema == "3":  # Películas
                new_values["nombre_peli"] = input("Ingrese el nuevo nombre de la película (deje en blanco para mantener el actual): ")
                new_values["director"] = input("Ingrese el nuevo director (deje en blanco para mantener el actual): ")
                new_values["genero_pelicula"] = input("Ingrese el nuevo género de la película (deje en blanco para mantener el actual): ")
            else:  # Default (Examen Tercer Parcial)
                new_values["CURP"] = input("Ingrese el nuevo CURP (deje en blanco para mantener el actual): ")
                new_calificacion = input("Ingrese la nueva calificación (deje en blanco para mantener la actual): ")
                new_values["calificacion"] = float(new_calificacion) if new_calificacion else None
                new_values["materia"] = input("Ingrese la nueva materia (deje en blanco para mantener el actual): ")

            # Eliminar claves vacías
            update_query = {k: v for k, v in new_values.items() if v != ""}
            
            # Actualizar el documento
            result = collection.update_one({"_id": document_to_update["_id"]}, {"$set": update_query})
            if result.modified_count > 0:
                print("Documento actualizado exitosamente.")
                time.sleep(1)
                clear_console()
            else:
                print("No se realizaron cambios en el documento.")
        else:
            print("Número de documento inválido. Operación cancelada.")
    except ValueError:
        print("Entrada inválida. Operación cancelada.")

