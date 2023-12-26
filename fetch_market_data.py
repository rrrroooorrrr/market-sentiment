import yfinance as yf
import csv

def write_to_csv(stock_data, filename):
    # Open the file in write mode
    with open(filename, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.DictWriter(file, fieldnames=stock_data[0].keys())
        
        # Write the header
        writer.writeheader()
        
        # Write the stock data
        for row in stock_data:
            writer.writerow(row)

def fetch_market_data(ticker, start_date, end_date):
    print(f'Fetching {ticker} data...')
    data = yf.download(ticker, start=start_date, end=end_date, group_by=ticker)
    return data

# market_data = get_market_data('SPY', '2020-01-01', '2023-01-01')
