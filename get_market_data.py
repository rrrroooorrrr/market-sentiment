import yfinance as yf
import pandas as pd
def get_market_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Example: Fetch SPY data
spy_data = get_market_data('SPY', '2020-01-01', '2023-01-01')

print(spy_data)