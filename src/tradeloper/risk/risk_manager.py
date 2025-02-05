class RiskManager:
    """
    Quantifies risk and determines if an order should be executed.
    """
    def __init__(self, max_position_size=1000, max_drawdown=0.2):
        self.max_position_size = max_position_size
        self.max_drawdown = max_drawdown

    def evaluate_risk(self, current_position, proposed_order):
        """
        Evaluate if the proposed order is within acceptable risk limits.
        current_position: current number of shares (positive for long, negative for short)
        proposed_order: dictionary with order details, e.g. {'side': 'buy', 'quantity': ...}
        Returns True if the order is acceptable; otherwise, False.
        """
        new_position = current_position
        if proposed_order['side'] == 'buy':
            new_position += proposed_order['quantity']
        elif proposed_order['side'] == 'sell':
            new_position -= proposed_order['quantity']

        # Reject if new position exceeds maximum allowed size.
        if abs(new_position) > self.max_position_size:
            return False

        # Additional risk evaluations (e.g., drawdown, volatility) can be added here.
        return True
