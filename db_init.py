from pymongo import MongoClient
def init_db(db_name):
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client[db_name]
    
        return db
    except Exception as e:
        print(f'DB Connection Failed: {e}')