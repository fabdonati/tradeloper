from copy import deepcopy

class Backtester:
    """
    Backtests trading strategies on historical data.
    """
    def __init__(self, data_handler, strategy_manager, risk_manager):
        self.data_handler = data_handler
        self.strategy_manager = strategy_manager
        self.risk_manager = risk_manager
        self.initial_capital = 100000  # Starting capital

    def run_backtest(self, symbol, start_date, end_date):
        """
        Run the backtest for a given symbol over a specified date range.
        Simulates trade execution based on strategy signals and risk management.
        """
        data = self.data_handler.get_historical_data(symbol, start_date, end_date)
        current_capital = self.initial_capital
        current_position = 0
        trades = []

        # Loop over the data starting after the lookback period.
        lookback = self.strategy_manager.strategies[0].lookback
        for current_date in data.index[lookback:]:
            data_slice = data.loc[:current_date]
            signals = self.strategy_manager.generate_signal(symbol, data_slice)
            # For simplicity, we use the first strategy's signal.
            signal = list(signals.values())[0]

            order = None
            if signal == "buy":
                order = {"side": "buy", "quantity": 10, "price": data.loc[current_date, 'Price']}
            elif signal == "sell":
                order = {"side": "sell", "quantity": 10, "price": data.loc[current_date, 'Price']}
            else:
                continue

            # Use risk manager to decide if we can execute the order.
            if self.risk_manager.evaluate_risk(current_position, order):
                if order["side"] == "buy":
                    current_capital -= order["quantity"] * order["price"]
                    current_position += order["quantity"]
                elif order["side"] == "sell":
                    current_capital += order["quantity"] * order["price"]
                    current_position -= order["quantity"]

                trades.append({
                    "date": current_date,
                    "order": deepcopy(order),
                    "capital": current_capital,
                    "position": current_position
                })

        return trades
