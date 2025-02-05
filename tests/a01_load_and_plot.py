
# Fetch historical data for AAPL from Yahoo Finance
from tradeloper.data.data_handler import DataHandler
from tradeloper.plot.plotter import StockPlotter


data_source = "yahoo"
symbol = "AAPL"
start_date = "2023-01-01"
end_date = "2024-02-01"

# Load data
handler = DataHandler(data_source=data_source)
df = handler.get_historical_data(symbol, start_date, end_date)

# Plot data
plotter = StockPlotter(df)
plotter.plot_prices()
plotter.plot_returns()
plotter.plot_candlestick()
plotter.plot_moving_average(window=10)


