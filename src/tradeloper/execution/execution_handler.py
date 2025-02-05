from ib_insync import IB, Stock, MarketOrder

class ExecutionHandler:
    """
    Handles sending orders to a live trading platform using the IBKR API.
    """
    def __init__(self, host='127.0.0.1', port=7497, clientId=1):
        self.ib = IB()
        self.host = host
        self.port = port
        self.clientId = clientId
        self.connect()

    def connect(self):
        self.ib.connect(self.host, self.port, clientId=self.clientId)

    def disconnect(self):
        self.ib.disconnect()

    def execute_order(self, symbol, order_details):
        """
        Execute an order for the given symbol.
        order_details: dictionary with keys like 'side' and 'quantity'.
        """
        contract = Stock(symbol, 'SMART', 'USD')

        if order_details['side'] == 'buy':
            order = MarketOrder('BUY', order_details['quantity'])
        elif order_details['side'] == 'sell':
            order = MarketOrder('SELL', order_details['quantity'])
        else:
            raise ValueError("Order side must be 'buy' or 'sell'")

        trade = self.ib.placeOrder(contract, order)
        return trade
