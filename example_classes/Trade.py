Symbol = str
UserId = str

class Trade:
    """
    Represents a single trade transaction on a trading platform.

    This class holds information about a trade, including the symbol of the traded asset, 
    the price at which the trade was executed, the quantity of the asset traded, the IDs of the buyer 
    and seller, and the timestamp of when the trade occurred.

    :param symbol: The trading symbol of the asset.
    :type symbol: Symbol (alias for str)
    :param price: The price at which the trade was executed.
    :type price: int
    :param quantity: The quantity of the asset traded.
    :type quantity: int
    :param buyer: The ID of the buyer, optional.
    :type buyer: UserId (alias for str), optional
    :param seller: The ID of the seller, optional.
    :type seller: UserId (alias for str), optional
    :param timestamp: The timestamp when the trade occurred, defaults to 0.
    :type timestamp: int, optional
    """
    def __init__(self, symbol: Symbol, price: int, quantity: int, buyer: UserId = None, seller: UserId = None, timestamp: int = 0) -> None:
        """
        Initializes a new instance of the Trade class.
        """
        self.symbol = symbol
        self.price: int = price
        self.quantity: int = quantity
        self.buyer = buyer
        self.seller = seller
        self.timestamp = timestamp

    def __str__(self) -> str:
        """
        Returns a string representation of the Trade instance.

        :return: A string that represents the trade.
        :rtype: str
        """
        return f"({self.symbol}, {self.buyer} << {self.seller}, {self.price}, {self.quantity}, {self.timestamp})"
    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the Trade instance, suitable for debugging.

        :return: A detailed string that represents the trade.
        :rtype: str
        """
        return "(" + self.symbol + ", " + self.buyer + " << " + self.seller + ", " + str(self.price) + ", " + str(self.quantity) + ", " + str(self.timestamp) + ")" + self.symbol + ", " + self.buyer + " << " + self.seller + ", " + str(self.price) + ", " + str(self.quantity) + ")"