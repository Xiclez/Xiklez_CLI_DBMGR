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
            return input("Elija condición de búsqueda:\n1. titulo\n2. clasificacion\n3. genero\nIngrese su elección (1-3): "), ["titulo", "clasificacion", "genero"]
        elif schema == "2":  # Música
            return input("Elija condición de búsqueda:\n1. nombre_cancion\n2. Album\n3. genero_musical\nIngrese su elección (1-3): "), ["nombre_cancion", "Album", "genero_musical"]
        elif schema == "3":  # Películas
            return input("Elija condición de búsqueda:\n1. nombre_peli\n2. director\n3. genero_pelicula\nIngrese su elección (1-3): "), ["nombre_peli", "director", "genero_pelicula"]
        else:  # Default (Examen Tercer Parcial)
            return input("Elija condición de búsqueda:\n1. CURP\n2. calificacion\n3. materia\nIngrese su elección (1-3): "), ["CURP", "calificacion", "materia"]

    header, fields = prompt_search_options(schema)
    if header not in ["1", "2", "3"]:
        print("Error: Ingrese una opción correcta")
        return None

    query = input("Ingrese término a buscar: ")
    field = fields[int(header) - 1]
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