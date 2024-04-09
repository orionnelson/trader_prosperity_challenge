from typing import List, Dict, NamedTuple

class PriceVolume(NamedTuple):
    price: float
    volume: int

class TradeData(NamedTuple):
    timestamp: int
    buyer: str
    seller: str
    symbol: str
    currency: str
    price: float
    quantity: int

class Listing:
    """
    Represents a tradable product or asset within the trading environment, including detailed
    information on bid and ask prices, volumes, and historical trades.

    :param symbol: The unique identifier or symbol for the tradable product.
    :param product: The name of the product.
    :param denomination: The unit of trade or currency in which this product is traded.
    """
    def __init__(self, symbol: str, product: str, denomination: str):
        self.symbol = symbol
        self.product = product
        self.denomination = denomination
        self.bid_prices: List[PriceVolume] = []
        self.ask_prices: List[PriceVolume] = []
        self.trades: List[TradeData] = []

    def update_market_depth(self, bid_prices: Dict[float, int], ask_prices: Dict[float, int]):
        """
        Updates the market depth for the listing with new bid and ask information.

        :param bid_prices: A dictionary mapping bid prices to volumes.
        :param ask_prices: A dictionary mapping ask prices to volumes.
        """
        self.bid_prices = [PriceVolume(price, volume) for price, volume in bid_prices.items()]
        self.ask_prices = [PriceVolume(price, volume) for price, volume in ask_prices.items()]
        self.bid_prices.sort(key=lambda x: x.price, reverse=True)  # Highest bid first
        self.ask_prices.sort(key=lambda x: x.price)  # Lowest ask first

    def record_trade(self, trade_data: TradeData):
        """
        Records a trade for the listing.

        :param trade_data: The trade data to record.
        """
        self.trades.append(trade_data)

    def __repr__(self) -> str:
        return f"Listing(symbol={self.symbol}, product={self.product}, denomination={self.denomination})"
