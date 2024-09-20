import yfinance as yf

def get_yf_data():

    # Download historical data for a stock (e.g., AAPL)
    data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

    return data
