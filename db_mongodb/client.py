from sys import argv
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6"

def test_db(host: str = 'localhost', port: int = 27017, db_name: str = "Test"):
    db = Client(host, port, db_name).get_db()
    if db.connection:
        print("[TEST] db connection result set: %s" % db.connection)
        return True
    else:
        print("[TEST] db connection result set: %s" % db.connection)
        return False

class Column:
    def __init__(self, column_type, primary_key=False, unique=False, nullable=True, default=None):
        self.column_type = column_type
        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.default = default

class Client(object):
    def __init__(self, host: str = 'localhost',
                 port: int = 27017,
                 db_name: str = None):

        self._client = MongoClient(f'mongodb://{host}:{port}')
        self._db = self._client[db_name]

    def get_db(self):
        return self._db

    def get_collection(self, collection_name: str):
        return self.get_db()[collection_name]

    def create_collection(self, collection_name: str):
        return self.get_db().create_collection(collection_name)
    
    def drop_collection(self, collection_name: str):
        return self.get_db().drop_collection(collection_name)

    def set_data_collection(self, collection_name: str, data: dict):
        return self.get_db()[collection_name].insert_one(data)

    def add(self, data):
        pass

    @staticmethod
    def Column(column_type, primary_key=False, unique=False, nullable=True, default=None):
        return Column(str(column_type), primary_key=primary_key, unique=unique, nullable=nullable, default=default)


if __name__ == "__main__":
    test_db(*argv)