import pymongo

def get_connection_data():

    pingu = """
    
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' 
    """

    # ASCII Art para el mensaje de bienvenida
    welcome_message = """
   
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

██╗░░██╗██╗██╗░░██╗██╗░░░░░███████╗███████╗  ██████╗░██████╗░  ███╗░░░███╗░██████╗░██████╗░
╚██╗██╔╝██║██║░██╔╝██║░░░░░██╔════╝╚════██║  ██╔══██╗██╔══██╗  ████╗░████║██╔════╝░██╔══██╗
░╚███╔╝░██║█████═╝░██║░░░░░█████╗░░░░███╔═╝  ██║░░██║██████╦╝  ██╔████╔██║██║░░██╗░██████╔╝
░██╔██╗░██║██╔═██╗░██║░░░░░██╔══╝░░██╔══╝░░  ██║░░██║██╔══██╗  ██║╚██╔╝██║██║░░╚██╗██╔══██╗
██╔╝╚██╗██║██║░╚██╗███████╗███████╗███████╗  ██████╔╝██████╦╝  ██║░╚═╝░██║╚██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝  ╚═════╝░╚═════╝░  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝
    """
    print(pingu)
    print(welcome_message)

    use_default = input("¿Quieres usar la base de datos de Xiklez? (y/n): ").lower()

    if use_default == 'n':
        db_url = input("Ingresa la cadena de conexión a tu base de datos: ")
    else:
        db_url = "mongodb+srv://6614:ulsapw2023@ulsa.cpqqpie.mongodb.net/"

    schema = input("Elige el template para tu base de datos:\n0. Examen tercer parcial:{'CURP','calificacion','materia'}\n1. Videojuegos: {'titulo','clasificacion','genero'}\n2. Música: {'nombre_cancion','Album','genero_musical'}\n3. Películas: {'nombre_peli','director','genero_pelicula'}")

    database = input("¿Cuál será el nombre de tu base de datos? ")
    collection_name = input("Por último, la colección: ")

    return db_url, database, collection_name, schema

def connect_to_mongodb(db_url, database, collection_name):
    try:
        client = pymongo.MongoClient(db_url)
        db = client[database]
        collection = db[collection_name]
        return client, collection
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error al conectar la base de datos: {e}")
        return None, None
#CRUD

#Create
def insert_document(collection, schema):
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
#Read   
def print_collection_content(collection):
    documents = collection.find()
    for document in documents:
        print(document)

def search_document(collection, schema, print_results=False):
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
#Update
def update_document(collection, schema):
    documents = search_document(collection, schema, print_results=True)
    if documents is None or len(documents) == 0:
        return

    # Listar los documentos y pedir al usuario que elija uno para actualizar
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
            
            # Pedir al usuario que ingrese los nuevos valores
            # Aquí, puedes añadir o modificar los campos según tus necesidades y esquema de base de datos
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
            else:
                print("No se realizaron cambios en el documento.")
        else:
            print("Número de documento inválido. Operación cancelada.")
    except ValueError:
        print("Entrada inválida. Operación cancelada.")

#Delete
def delete_document(collection, schema):
    documents = search_document(collection, schema, print_results=True)
    if documents is None or len(documents) == 0:
        return

    # Opciones de eliminación
    print("\nSeleccione el documento que desea eliminar:")
    for i, doc in enumerate(documents):
        print(f"{i + 1}. {doc}")
    print("0. Cancelar")
    print("99. Eliminar todos los documentos encontrados")

    try:
        choice = int(input("\nIngrese su elección: "))
        if choice == 0:
            print("Eliminación cancelada.")
            return
        elif choice == 99:
            # Confirmar antes de eliminar todos
            confirm = input("¿Está seguro de que desea eliminar TODOS los documentos encontrados? (y/n): ")
            if confirm.lower() == 'y':
                ids_to_delete = [doc["_id"] for doc in documents]
                result = collection.delete_many({"_id": {"$in": ids_to_delete}})
                print(f"{result.deleted_count} documentos eliminados exitosamente.")
            else:
                print("Eliminación cancelada.")
        elif 1 <= choice <= len(documents):
            document_to_delete = documents[choice - 1]
            confirm = input(f"¿Está seguro de que desea eliminar el documento con ID '{document_to_delete['_id']}'? (y/n): ")
            if confirm.lower() == 'y':
                result = collection.delete_one({"_id": document_to_delete["_id"]})
                if result.deleted_count > 0:
                    print("Documento eliminado exitosamente.")
                else:
                    print("Error al intentar eliminar el documento.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Número de documento inválido. Operación cancelada.")
    except ValueError:
        print("Entrada inválida. Operación cancelada.")


def menu():

    crud= """
  /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$ 
 /$$__  $$| $$__  $$| $$  | $$| $$__  $$
| $$  \__/| $$  \ $$| $$  | $$| $$  \ $$
| $$      | $$$$$$$/| $$  | $$| $$  | $$
| $$      | $$__  $$| $$  | $$| $$  | $$
| $$    $$| $$  \ $$| $$  | $$| $$  | $$
|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/
 \______/ |__/  |__/ \______/ |_______/                                   
    """
    print(crud)
    print("1. Imprimir contenido de la colección")
    print("2. Buscar un documento")
    print("3. Insertar un documento")
    print("4. Actualizar un documento")
    print("5. Eliminar un documento")
    print("6. Salir")

def main():
    db_url, database, collection_name, schema = get_connection_data()
    client, collection = connect_to_mongodb(db_url, database, collection_name)

    if client is None or collection is None:
        print("Error en la conexión. Saliendo del programa.")
        return

    while True:
        menu()
        option = input("Seleccione la opción deseada (1-6): ")

        if option == "1":
            print_collection_content(collection)
        elif option == "2":
            search_document(collection, schema,print_results=True)
        elif option == "3":
            insert_document(collection, schema)
        elif option == "4":
            update_document(collection, schema)
        elif option == "5":
            delete_document(collection, schema)
        elif option == "6":
            print("Gracias por usar Xiklez CLI DBMGR, hasta pronto! :)")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 6.")

    client.close()

if __name__ == "__main__":
    main()