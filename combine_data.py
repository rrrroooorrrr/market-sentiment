import pandas as pd
import matplotlib.pyplot as plt
from fetch_market_data import fetch_market_data

def combine_data(sentiment_data, market_data):
    # If 'Date' is an index in market_data, reset it
    if market_data.index.name == 'Date':
        market_data.reset_index(inplace=True)
    
    # Merge the data on 'Date'
        
    sentiment_data['Date'] = pd.to_datetime(sentiment_data['Date'])
    if 'Date' in market_data.columns:
        market_data['Date'] = pd.to_datetime(market_data['Date'])
    else:
        market_data.reset_index(inplace=True)
        market_data['Date'] = pd.to_datetime(market_data['Date'])

    combined = pd.merge(sentiment_data, market_data, on='Date')

    # Ensure you return the combined data
    return combined

# Example usage
sentiment_data = pd.read_csv('2023-12-25_sentiment.csv')
market_data = fetch_market_data('SPY', '2020-01-01', '2023-01-01')
combined_data = combine_data(sentiment_data, market_data)

# Basic Exploratory Data Analysis
plt.figure(figsize=(12, 6))
plt.plot(combined_data['Date'], combined_data['sentiment_score'], label='Sentiment Score')
plt.plot(combined_data['Date'], combined_data['Close'], label='Market Close Price')
plt.title('Sentiment Score vs Market Close Price Over Time')
plt.xlabel('Date')
plt.legend()
plt.show()

# Statistical Analysis
correlation = combined_data['sentiment_score'].corr(combined_data['Close'])
print(f"Correlation between sentiment score and market close price: {correlation}")
