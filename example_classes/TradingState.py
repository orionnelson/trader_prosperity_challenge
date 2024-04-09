from typing import Dict, List
import json
from example_classes.Listing import Listing
from example_classes.OrderDepth import OrderDepth
from example_classes.Trade import Trade 

Time = int
Symbol = str
Product = str
Position = int

class TradingState(object):
    """
    Represents the current state of trading, encapsulating all relevant data for trading decisions.
    
    This includes data on listings, order depths, trades, positions, and any other observations relevant
    to the trading environment. It also includes trader-specific data that could influence decision-making.
    
    :param traderData: Custom data relevant to the trader's current state.
    :type traderData: str
    :param timestamp: The current timestamp of the trading state.
    :type timestamp: Time
    :param listings: A dictionary of listings by product symbol.
    :type listings: Dict[Symbol, Listing]
    :param order_depths: A dictionary of order depths by product symbol.
    :type order_depths: Dict[Symbol, OrderDepth]
    :param own_trades: A dictionary of trades initiated by the trader, by product symbol.
    :type own_trades: Dict[Symbol, List[Trade]]
    :param market_trades: A dictionary of market trades, by product symbol.
    :type market_trades: Dict[Symbol, List[Trade]]
    :param position: A dictionary of the trader's current positions, by product.
    :type position: Dict[Product, Position]
    :param observations: Miscellaneous observations relevant to the trading state.
    :type observations: Observation
    
    The class provides a method to serialize its attributes to JSON for easy storage or transmission.
    """
    def __init__(self,
                 traderData: str,
                 timestamp: Time,
                 listings: Dict[Symbol, Listing],
                 order_depths: Dict[Symbol, OrderDepth],
                 own_trades: Dict[Symbol, List[Trade]],
                 market_trades: Dict[Symbol, List[Trade]],
                 position: Dict[Product, Position],
                 observations: Observation):
        self.traderData = traderData
        self.timestamp = timestamp
        self.listings = listings
        self.order_depths = order_depths
        self.own_trades = own_trades
        self.market_trades = market_trades
        self.position = position
        self.observations = observations
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)