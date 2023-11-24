import pymongo

def connect_to_mongodb(db_url, database, collection_name):
    try:
        client = pymongo.MongoClient(db_url)
        db = client[database]
        collection = db[collection_name]
        return client, collection
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error al conectar la base de datos: {e}")
        return None, None