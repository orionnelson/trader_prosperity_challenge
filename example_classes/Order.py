Symbol = str
"""
A type alias for representing a stock symbol or identifier in trading operations.
"""

class Order:
    """
    Represents a trading order for a specific product identified by its symbol.
    
    A trading order consists of a symbol for the product to be traded, the price at which
    the trade should occur, and the quantity of the product to trade. This class provides
    a structured way to encapsulate this information.

    :param symbol: The symbol representing the product to be traded.
    :type symbol: Symbol
    :param price: The price at which the product should be bought or sold.
    :type price: int
    :param quantity: The quantity of the product to be traded.
    :type quantity: int
    """
    def __init__(self, symbol: Symbol, price: int, quantity: int) -> None:
        """
        Initializes a new Order instance.

        :param symbol: The trading symbol for the order.
        :param price: The price per unit for the order.
        :param quantity: The number of units to be traded.
        """
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Returns a string representation of the Order.

        :return: A string that represents the order's symbol, price, and quantity.
        """
        return f"({self.symbol}, {self.price}, {self.quantity})"

    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the Order suitable for debugging.

        :return: A string that represents the order's symbol, price, and quantity, identical to __str__.
        """

        return f"({self.symbol}, {self.price}, {self.quantity})"