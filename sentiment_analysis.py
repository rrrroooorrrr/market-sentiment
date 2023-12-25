import schedule
import time
import nltk
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline
from fetch_rss import fetch_rss
from store_sentiment_data import write_to_db, write_to_csv
from format_dates import convert_to_standard_format



# Download necessary NLTK data
def download_nltk_data():
    nltk.download('vader_lexicon') 

# Initialize NLP models
vader_analyzer = SentimentIntensityAnalyzer()
bert_model = pipeline('sentiment-analysis', model='bert-base-uncased')
processed_articles = []

def analyze_sentiment(article_text):
    # Vader
    vader_score = vader_analyzer.polarity_scores(article_text)['compound']

    # TextBlob
    textblob_score = TextBlob(article_text).sentiment.polarity

    # Hugging Face Model (BERT)
    bert_score = bert_model(article_text)[0]['score']

    # Aggregate scores - adjust weights as needed
    combined_score = (vader_score + textblob_score + bert_score) / 3
    return combined_score

def process_news():
    articles = fetch_rss() 
    print('Analyzing Sentiment...')
    for article in articles:
        sentiment_score = analyze_sentiment(article['summary'])
        article['date'] = convert_to_standard_format(article['published'])
        article['sentiment_score']=sentiment_score
        article['median_sentiment_score']=''
        article['average_sentiment_score']=''
        del article['published']
        
        processed_articles.append(article)
    
    print('Sentiment analysis complete...')
     # Calculate median and average sentiment scores
    scores = [article['sentiment_score'] for article in processed_articles]
    median = np.median(scores)
    avg    = np.mean(scores)

    write_to_db(processed_articles, median, avg)
    write_to_csv(processed_articles, median, avg)

def main():
    download_nltk_data()
    # schedule.every(15).minutes.do(process_news)
    # schedule.every().day.at("16:00").do(write_to_csv)
    # schedule.every().day.at("16:00").do(write_to_db)
    process_news()
        

    while True:
            schedule.run_pending()
            time.sleep(60)  # Sleep to avoid tight looping

if __name__ == "__main__":
    main()
