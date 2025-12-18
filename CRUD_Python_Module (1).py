# Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        """
        Initialize MongoClient using the provided username and password.
        Connects to the 'aac' database and 'animals' collection.
        """
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}/')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return bool(result.inserted_id)
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise Exception("Nothing to save. Data parameter is empty.")

    def read(self, query):
        if query is not None:
            try:
                cursor = self.collection.find(query)
                results = list(cursor)
                return results
            except Exception as e:
                print(f"Error reading documents: {e}")
                return []
        else:
            raise Exception("Query parameter is empty.")

    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            raise Exception("Query or new_values parameter is empty.")

    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Error deleting documents: {e}")
                return 0
        else:
            raise Exception("Query parameter is empty.")

            