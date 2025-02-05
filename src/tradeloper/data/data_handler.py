import pandas as pd
import yfinance as yf  # Example for fetching historical data
import matplotlib.pyplot as plt


class DataHandler:
    """
    Handles data ingestion from historical sources and live market data.
    """
    def __init__(self, data_source='yahoo'):
        self.data_source = data_source

    def get_historical_data(self, symbol, start_date, end_date):
        """
        Retrieve historical data for a given symbol between start_date and end_date.
        Supports multiple data sources.
        """
        if self.data_source == 'yahoo':
            try:
                data = yf.download(symbol, start=start_date, end=end_date)
                return data
            except Exception as e:
                print(f"Error fetching data: {e}")
                return None
        else:
            raise ValueError(f"Data source {self.data_source} not supported")

    def get_live_data(self, symbol):
        """
        Retrieve live market data for a given symbol.
        TODO: Implement real-time data retrieval using a broker API (e.g., IBKR, Alpaca).
        """
        raise NotImplementedError("Live data retrieval not yet implemented.")

# Example Usage:
if __name__ == "__main__":
        
    # Fetch historical data for AAPL from Yahoo Finance
    data_source = "yahoo"
    symbol = "AAPL"
    start_date = "2020-01-01"
    end_date = "2024-02-01"

    handler = DataHandler(data_source=data_source)
    df = handler.get_historical_data(symbol, start_date, end_date)
    print(df.head())

    # Plot the historical price data
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Price'], marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title(f'{symbol} Historical Price Data')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()