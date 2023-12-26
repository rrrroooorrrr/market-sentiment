import csv
import datetime
import db_init

def write_to_db(processed_articles, median, avg):
    if processed_articles:
        try:
            # Initialize DB connection
            db = db_init.init_db()

            # Create a new collection name based on the current date
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            collection_name = f"{current_date}_sentiment"
            collection = db[collection_name]

            summary_document = {
                'date': current_date,
                'median_sentiment_score': median,
                'average_sentiment_score': avg
            }

            # Insert articles and summary into the collection
            collection.insert_many(processed_articles)
            collection.insert_one(summary_document)

            print('Data written to DB successfully...')

        except Exception as e:
            print(f"DB Write Error: {e}")

def write_to_csv(processed_articles, median, avg):
    if processed_articles:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_name = f"results/{current_date}_sentiment.csv"
        print(f'Writing CSV output: {file_name}')
        
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['_id', 'title', 'link', 'Date', 'summary', 'sentiment_score', 'median_sentiment_score', 'average_sentiment_score']

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            # add median and avg to first row
            first_article = processed_articles[0]
            first_article['median_sentiment_score'] = median
            first_article['average_sentiment_score'] = avg
            writer.writerow(first_article)
            
            writer.writerows(processed_articles[1:])
        



