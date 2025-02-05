class StrategyManager:
    """
    Manages a collection of trading strategies.
    """
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def generate_signal(self, symbol, data):
        """
        For each strategy, generate a signal for the given symbol and data.
        Returns a dictionary mapping strategy names to signals.
        """
        signals = {}
        for strategy in self.strategies:
            signals[strategy.name] = strategy.generate_signal(symbol, data)
        return signals

class MeanReversionStrategy:
    """
    An example mean reversion strategy.
    """
    def __init__(self, lookback=20, threshold=1.5):
        self.lookback = lookback
        self.threshold = threshold
        self.name = "MeanReversion"

    def generate_signal(self, symbol, data):
        """
        Generate a trading signal ('buy', 'sell', or 'hold') based on mean reversion logic.
        This dummy implementation uses rolling averages.
        """
        if len(data) < self.lookback:
            return "hold"

        moving_average = data['Price'].rolling(window=self.lookback).mean().iloc[-1]
        current_price = data['Price'].iloc[-1]

        if current_price < moving_average - self.threshold:
            return "buy"
        elif current_price > moving_average + self.threshold:
            return "sell"
        else:
            return "hold"
