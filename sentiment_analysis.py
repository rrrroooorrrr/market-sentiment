# import schedule
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline
# Additional imports for database and error handling
from db_stuff import db_init
from fetch_rss import fetch_news
from store_data import store_db, store_csv
# Establishing a connection to the MongoDB database
nltk.downloader.download('vader_lexicon')



vader_analyzer = SentimentIntensityAnalyzer()
bert_model = pipeline('sentiment-analysis', model='bert-base-uncased')



def analyze_sentiment(article_text):
   # Vader
    vader_score = vader_analyzer.polarity_scores(article_text)['compound']

    # TextBlob
    textblob_score = TextBlob(article_text).sentiment.polarity

    # Hugging Face Model (BERT)
    bert_score = bert_model(article_text)[0]['score']

    # Aggregate scores - you can adjust the weights as needed
    combined_score = (vader_score + textblob_score + bert_score) / 3
    return combined_score

def process_news(articles, collection):
    for article in articles:
        sentiment_score = analyze_sentiment(article['text'])
        print({article, sentiment_score})
        store_csv(article)
        store_db(collection, article, sentiment_score)
        


def main():
    db_connected = False
    collection = None
    try: 
        collection = db_init.init_db
        db_connected = True
    except:
        print('connection failed')
   
    if db_connected:
        articles = fetch_news() 
        process_news(articles, collection)

    # schedule.every(15).minutes.do(process_news)

    # while True:
    #     schedule.run_pending()
    #     sleep(60)  # Sleep to avoid tight looping

if __name__ == "__main__":
    main()
