#Delete
from .read import search_document
from utils.clear_console import clear_console
from utils.ascii_arts import draw_delete

def delete_document(collection, schema):
    clear_console()
    print(draw_delete())
    documents = search_document(collection, schema, print_results=True)
    if documents is None or len(documents) == 0:
        return

  
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


