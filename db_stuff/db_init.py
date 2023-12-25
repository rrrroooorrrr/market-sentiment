from pymongo import MongoClient
def init_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.news_database  # 'news_database' is the database name
    collection = db.articles   # 'articles' is the collection name
    print('db connected')
    return collection
        