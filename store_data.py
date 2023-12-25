import csv
import datetime



def store_db(collection, article_data, sentiment_score):
    for article in article_data:
        # Adding sentiment score to the article data
        article['title'] = sentiment_score

        # Storing the article in the database
        collection.insert_one(article)

def store_csv(data):
    # Get the current date in YYYY-MM-DD format
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f"{current_date}_sentiment.csv"

    # Field names (keys of your data dictionaries)
    fieldnames = ['title', 'link', 'published', 'summary', 'sentiment_score']

    # Writing to csv file
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        for article in data:
            writer.writerow(article)

