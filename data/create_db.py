from utils.clear_console import clear_console
from utils.ascii_arts import draw_pingu
from utils.ascii_arts import draw_welcome_message
def create_db():
    print(draw_pingu())
    print(draw_welcome_message())

    use_default = input("¿Quieres usar la base de datos de Xiklez? (y/n): ").lower()

    if use_default == 'n':
        username = input("Ingresa el nombre de usuario de tu base de datos: ")
        password = input("Ingresa la contraseña de tu base de datos: ")
        cluster_name = input("Ingresa el nombre de tu clúster de MongoDB Atlas: ")
        db_url = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/"
    else:
        db_url = "mongodb+srv://6614:ulsapw2023@ulsa.cpqqpie.mongodb.net/"
    
    clear_console()
    print("Elige el template para tu base de datos:\n0. Examen tercer parcial:{'CURP','calificacion','materia'}\n1. Videojuegos: {'titulo','clasificacion','genero'}\n2. Música: {'nombre_cancion','Album','genero_musical'}\n3. Películas: {'nombre_peli','director','genero_pelicula'}")
    schema = input("Elige una opción (0-3): ")
    clear_console()
    print("Excelente elección! :)")
    if schema == "1":
        print("Videojuegos")
    elif schema == "2":
        print("Música")
    elif schema == "3":
        print("Películas")
    else:
        print("Ulsa")
    database = input("¿Cuál será el nombre de tu base de datos? ").strip().replace(" ", "_")
    collection_name = input("Por último, la colección: ").strip().replace(" ", "_")

    return db_url, database, collection_name, schema


