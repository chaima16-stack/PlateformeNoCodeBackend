from pymongo import MongoClient
from bson import ObjectId

MONGO_URI = f"mongodb://localhost:27017/NCP_DataBase"
def connect_to_mongo():
        client = MongoClient(MONGO_URI)
        return client
    
def deconnect_from_mongo(client):
         client.close()

def create_dataBase(client,db_name):
    try:
      db= client[db_name]
      return db
    except Exception as e:
        return False, f"ERROR CREATION : {str(e)}"
    finally:
        client.close()
    

def Create_collection(db_name,collection_name):
    try:
         client = connect_to_mongo()
         db= client[db_name]
         db.create_collection(collection_name)
         return True, f"Collection CREATED SUCCESSFULLY."
    except Exception as e:
        return False, f"ERROR CREATION: {str(e)}"
    finally:
        client.close()


# Fonction pour ajouter  à une collection existante
def insert_to_collection(db_name, collection_name, body):
    try:
        # Connectez-vous à MongoDB
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        collection.insert_one(body)
        return True, "Attributes INSERTED SUCCESSFULLY."
    except Exception as e:
        return False, f"ERROR INSERT: {str(e)}"
    finally:
        client.close()


def rename_collection(db_name, old_collection_name, new_collection_name):
    try:
        # Se connecter à MongoDB
        client = connect_to_mongo()
        db = client[db_name]
        # Copier les documents de l'ancienne collection vers la nouvelle
        old_collection = db[old_collection_name]
        db.create_collection(new_collection_name)
        new_collection = db[new_collection_name]
        if old_collection.estimated_document_count() != 0 :
            new_collection.insert_many(old_collection.find())
        db.drop_collection(old_collection_name)
        client.close()
        return True, "UPDATED SUCCESSFULLY."
    except Exception as e:
        return False, f"ERROR UPDATE: {str(e)}"
    finally:
        client.close()

def rename_database(old_db_name, new_db_name):
    try:
        client = connect_to_mongo()
        # Créer une nouvelle base de données avec le nouveau nom
        old_db = client[old_db_name]
        new_db = client[new_db_name]
        for collection_name in old_db.list_collection_names():
            old_collection = old_db[collection_name]
            new_collection = new_db[collection_name]
            new_collection.insert_many(old_collection.find())
        client.drop_database(old_db_name)

        return True, "UPDATED SUCCESSFULLY"
    except Exception as e:
        return False, f"ERROR UPDATE : {str(e)}"
    finally:
        client.close()

def update_document(db_name, collection_name,id, update_data):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        filter_query = {"_id": ObjectId(id)}
        # Mettre à jour le document
        collection.update_one(filter_query, {"$set": update_data})
        
        return True, "SUCCEESSFULLY UPDATED"
    except Exception as e:
        return False, f"ERROR UPDATE : {str(e)}"
    finally:
        client.close()
def get_documents(db_name, collection_name):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        documents = list(collection.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])
            doc['id'] =  doc['_id']
            del doc['_id']
        """        # Obtenir les types des attributs pour chaque document
        documents_with_types = []
        for document in documents:
            document_with_types = {}
            for key, value in document.items():
                document_with_types[key] = type(value).__name__
            documents_with_types.append(document_with_types) """
        
        return True, documents
    except Exception as e:
        return False, f"ERROR OF LISTING : {str(e)}"
    finally:
        client.close()

def delete_collection(db_name, collection_name):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        collection.drop()
        
        return True, "SUCCEESSFULLY DELETED"
    except Exception as e:
        return False, f"ERROR DELETE : {str(e)}"
    finally:
        client.close()

def delete_document(id,db_name, collection_name):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        filter_query = {"_id": ObjectId(id)}
        collection.delete_one(filter_query)
        
        return True, "SUCCEESSFULLY DELETED"
    except Exception as e:
        return False, f"ERROR DELETE : {str(e)}"
    finally:
        client.close()

def delete_attribut(db_name, collection_name,attribute):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        collection.update_many({}, {"$unset": {attribute: ""}})
        return True, "SUCCEESSFULLY DELETED"
    except Exception as e:
        return False, f"ERROR DELETE : {str(e)}"
    finally:
        client.close()

def rename_attribute_in_collection(db_name, collection_name, old_attribute_name, new_attribute_name):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        result = collection.update_many({}, {"$rename": {old_attribute_name: new_attribute_name}})
        
        return True, f"UPDATED SUCCESSFULLY"
    except Exception as e:
        return False, f"ERROR UPDATE: {str(e)}"
    finally:
        client.close()

def add_empty_attribute_to_collection(db_name, collection_name, new_attribute_name):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        result = collection.update_many({}, {"$set": {new_attribute_name: ""}})
        
        return True, f"INSERTED SUCCESSFULLY"
    except Exception as e:
        return False, f"ERROR INSERT : {str(e)}"
    finally:
        client.close()

def get_document_by_id(db_name, collection_name, document_id):
    try:
        client = connect_to_mongo()
        db = client[db_name]
        collection = db[collection_name]
        document_id = ObjectId(document_id)
        document = collection.find_one({"_id": document_id})
        if document:
            # Convertir l'ID en une chaîne de caractères
            document['_id'] = str(document['_id'])
            # Ajouter une clé 'id' avec la valeur de '_id' et supprimer '_id'
            document['id'] = document['_id']
            del document['_id']
        
        if document:
            return True, document
        else:
            return False, "Aucun document trouvé avec cet ID."
    except Exception as e:
        return False, f"Erreur lors de la récupération du document : {str(e)}"
    finally:
        client.close()