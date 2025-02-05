
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

class StockPlotter:
    def __init__(self, data):
        """
        Initialize with a DataFrame containing stock price data.
        Expected columns: ['Open', 'High', 'Low', 'Close']
        """
        self.data = data

    def plot_prices(self):
        """Plot the stock's closing prices over time."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data.index, self.data['Close'], label='Close Price', linestyle='-')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.title('Stock Price Over Time')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()
    
    def plot_returns(self):
        """Plot the daily returns."""
        returns = self.data['Close'].pct_change()
        plt.figure(figsize=(10, 5))
        plt.plot(self.data.index, returns, label='Daily Returns', linestyle='-', marker='o')
        plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
        plt.xlabel('Date')
        plt.ylabel('Returns')
        plt.title('Daily Returns Over Time')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()
        
            
    def plot_candlestick(self):
        """Plot a candlestick chart."""
        fig, ax = plt.subplots(figsize=(10, 5))

        for idx, row in self.data.iterrows():
            # Ensure idx is a datetime object
            date_num = mdates.date2num(idx.to_pydatetime())

            # Extract values as scalars (avoid Series issues)
            open_price = row['Open'].item()
            high_price = row['High'].item()
            low_price = row['Low'].item()
            close_price = row['Close'].item()

            # Determine candle color
            color = 'green' if close_price >= open_price else 'red'

            # Draw wicks (high-low range)
            ax.plot([date_num, date_num], [low_price, high_price], color=color, linewidth=1)

            # Draw candle body
            rect = Rectangle(
                (date_num - 0.2, min(open_price, close_price)),
                0.4, abs(close_price - open_price),
                color=color, alpha=0.7
            )
            ax.add_patch(rect)

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.title('Stock Candlestick Chart')
        plt.grid(True)
        plt.show()

    
    def plot_moving_average(self, window=10):
        """Plot the moving average along with the closing prices."""
        self.data[f'MA_{window}'] = self.data['Close'].rolling(window=window).mean()
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.data.index, self.data['Close'], label='Close Price', linestyle='-')
        plt.plot(self.data.index, self.data[f'MA_{window}'], label=f'{window}-Day MA', linestyle='--', linewidth=2)
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.title(f'{window}-Day Moving Average')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()
