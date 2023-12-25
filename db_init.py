from pymongo import MongoClient
def init_db():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.news_sentiment
    
        return db
    except Exception as e:
        print(f'DB Connection Failed: {e}')