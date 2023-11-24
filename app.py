import time

from data.create_db import create_db
from data.connect import connect_to_mongodb
from utils.clear_console import clear_console
from utils.menu import menu
from utils.anims.first_doc_anim import first_doc_anim
from crud.create import insert_document
from crud.read import print_collection_content
from crud.read import search_document
from crud.update import update_document
from crud.delete import delete_document

def main():
    db_url, database, collection_name, schema = create_db()
    client, collection = connect_to_mongodb(db_url, database, collection_name)

    if client is None or collection is None:
        print("Error en la conexión. Saliendo del programa.")
        return
    
    first_doc_anim()
    insert_document(collection, schema)

    while True:
        
        menu()
        option = input("Seleccione la opción deseada (1-5): ")

        if option == "1":
            insert_document(collection, schema)
        elif option == "2":
            sub_option = input("Seleccione:\n1. Leer un solo documento\n2. Leer todos los documentos\nIngrese su elección (1-2): ")
            if sub_option == "1":
                search_document(collection, schema, print_results=True)
            elif sub_option == "2":
                print_collection_content(collection)
            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al 2.")
        elif option == "3":
            update_document(collection, schema)
        elif option == "4":
            delete_document(collection, schema)
        elif option == "5":
            print("Gracias por usar el Xiklez_CLI_DBMGR. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

    client.close()

if __name__ == "__main__":
    main()
