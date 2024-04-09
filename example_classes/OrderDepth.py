from typing import Dict

class OrderDepth:
    """
    Represents the depth of buy and sell orders for a product at various price points.
    
    This class maintains separate dictionaries for buy and sell orders, where each dictionary's keys are
    price points and values are the quantities of orders at those prices. It's commonly used to analyze
    market liquidity and depth for specific trading instruments or products.
    
    :ivar buy_orders: A dictionary mapping price points to quantities for buy orders.
    :vartype buy_orders: Dict[int, int]
    :ivar sell_orders: A dictionary mapping price points to quantities for sell orders.
    :vartype sell_orders: Dict[int, int]
    """
    def __init__(self):
        """
        Initializes the OrderDepth object with empty dictionaries for buy and sell orders.
        """
        self.buy_orders: Dict[int, int] = {}
        self.sell_orders: Dict[int, int] = {}