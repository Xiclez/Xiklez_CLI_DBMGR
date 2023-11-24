from utils.clear_console import clear_console
from utils.ascii_arts import (
    draw_pingu,
    draw_welcome_message,
    draw_videogames,
    draw_movies,
    draw_music,
    draw_ulsa,
    draw_tercer_parcial
)
from utils.anims.createdb_anim import createdb_anim
def create_db():
    print(draw_pingu())
    print(draw_welcome_message())

    use_default = input("¿Quieres usar la base de datos de Xiklez? (y/n): ").lower()

    if use_default == 'n':
        db_url = input("Ingresa la cadena de conexión a tu base de datos: ")
    else:
        db_url = "mongodb+srv://6614:ulsapw2023@ulsa.cpqqpie.mongodb.net/"
    clear_console()
    print("Elige el template para tu base de datos:\n0. Examen tercer parcial:{'CURP','calificacion','materia'}\n1. Videojuegos: {'titulo','clasificacion','genero'}\n2. Música: {'nombre_cancion','Album','genero_musical'}\n3. Películas: {'nombre_peli','director','genero_pelicula'}")
    schema = input("Elige una opcion (0-3): ")
    clear_console()
    print("Excelente eleccion! :)")
    if schema == "1":
        print(draw_videogames())
    elif schema == "2":
        print(draw_music())
    elif schema == "3":
        print(draw_movies())
    else:
        print(draw_ulsa())
        print(draw_tercer_parcial())
    database = input("¿Cuál será el nombre de tu base de datos? ")
    collection_name = input("Por último, la colección: ")
    createdb_anim()

    return db_url, database, collection_name, schema

