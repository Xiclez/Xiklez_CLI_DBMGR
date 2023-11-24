#Read   
from utils.clear_console import clear_console
from utils.ascii_arts import draw_read

def print_collection_content(collection):
    clear_console()
    draw_read()
    documents = collection.find()
    for document in documents:
        print(document)

def search_document(collection, schema, print_results=False):
    clear_console()
    def prompt_search_options(schema):
        if schema == "1":  # Videojuegos
            return ["titulo", "clasificacion", "genero"]
        elif schema == "2":  # Música
            return ["nombre_cancion", "Album", "genero_musical"]
        elif schema == "3":  # Películas
            return ["nombre_peli", "director", "genero_pelicula"]
        else:  # Default (Examen Tercer Parcial)
            return ["CURP", "calificacion", "materia"]

    fields = prompt_search_options(schema)
    print("Elija condición de búsqueda:")
    for idx, field in enumerate(fields, 1):
        print(f"{idx}. {field}")
    header = input("Ingrese su elección (1-3): ")
    
    if header not in ["1", "2", "3"]:
        print("Error: Ingrese una opción correcta")
        return None

    # Solicitar el término de búsqueda
    query_input = input("Ingrese término a buscar: ")
    field = fields[int(header) - 1]
    
    # Si el campo es 'calificacion' y el esquema es el default, convierte el término a float
    if schema == "0" and field == "calificacion":
        try:
            query = float(query_input)
        except ValueError:
            print("La calificación debe ser un número.")
            return None
    else:
        query = query_input

    documents = list(collection.find({field: query}))

    if not documents:
        print("No se encontraron documentos con el criterio especificado.")
        sel = input("¿Desea intentarlo otra vez? (y/n): ")
        if sel.lower() == 'y':
            return search_document(collection, schema, print_results)
        return None

    if print_results:
        for doc in documents:
            print(doc)

    return documents
