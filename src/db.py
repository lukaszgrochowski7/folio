import yfinance
import requests
import datetime
import pandas as pd

crdate = datetime.datetime.now()

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
tabele = pd.read_html(url, storage_options={"User-Agent": "folio/0.1 (grochowski.lukasz777@gmail.com)"})

sp500 = tabele[0]
tickers =sp500['Symbol'].tolist()

print(tickers)
data = sp500.loc[sp500["Symbol"] == "AAPL", "Date added"].iloc[0]
print(data)
def get_stock_data(ticker):
    """
    Fetches historical stock data for a given ticker symbol between specified start and end dates.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple Inc.).
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical stock data.
    """
    try:
        # Fetch historical stock data using yfinance
        for symbol in tickers:
            data = sp500.loc[sp500["Symbol"] == symbol, "Date added"].iloc[0]

            stock_data = yfinance.download(symbol, start=data, end=crdate)
            
            export_stock_data_to_sql(stock_data)  # Export the fetched data to SQL
        print(stock_data.columns) # Print the column names of the fetched data
        return stock_data
    except Exception as e:
        print(f"An error occurred while fetching stock data: {e}")
        return None

def export_stock_data_to_sql(stock_data): 
    ...

get_stock_data(sp500[sp500['Symbol'] == 'MSFT'].index[0])
    