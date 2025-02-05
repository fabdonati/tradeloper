from data.data_handler import DataHandler
from strategy.strategy_manager import StrategyManager, MeanReversionStrategy
from risk.risk_manager import RiskManager
from backtesting.backtester import Backtester
 
def main():
    # Initialize modules.
    data_handler = DataHandler()
    strategy_manager = StrategyManager()
    mean_reversion = MeanReversionStrategy(lookback=20, threshold=1.5)
    strategy_manager.add_strategy(mean_reversion)
    risk_manager = RiskManager(max_position_size=1000, max_drawdown=0.2)
 
    # Run backtest.
    backtester = Backtester(data_handler, strategy_manager, risk_manager)
    trades = backtester.run_backtest(symbol="AAPL", start_date="2020-01-01", end_date="2020-12-31")
 
    # Output trades.
    for trade in trades:
        print(trade)
 
if __name__ == "__main__":
    main()