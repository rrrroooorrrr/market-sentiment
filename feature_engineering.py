import pandas as pd

def relative_strength_index(data, periods=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def bollinger_bands(data, window=20, num_of_std=2):
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_of_std)
    lower_band = rolling_mean - (rolling_std * num_of_std)
    return upper_band, lower_band

def vwap(data):
    q = data['Volume'] * data['Close']
    vwap = q.cumsum() / data['Volume'].cumsum()
    return vwap

def feature_engineering(data):
    # Short-term Moving Averages
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_10'] = data['Close'].rolling(window=10).mean()

    # Exponential Moving Averages
    data['EMA_5'] = data['Close'].ewm(span=5, adjust=False).mean()
    data['EMA_10'] = data['Close'].ewm(span=10, adjust=False).mean()

    # Relative Strength Index
    data['RSI'] = relative_strength_index(data, periods=14)

    # Bollinger Bands
    data['Upper_Band'], data['Lower_Band'] = bollinger_bands(data, window=20)

    # Volume Weighted Average Price (VWAP)
    data['VWAP'] = vwap(data)

    # Incorporate Trading Volume
    data['Volume_MA'] = data['Volume'].rolling(window=5).mean()  # 5-day Moving Average of Volume

    return data

# Assuming spy_data is your DataFrame with market data
spy_data = feature_engineering(spy_data)
