from . import OrderDepth, UserId, TradingState, Order, Observation
from typing import List
import string

class Trader:
    
    def run(self, state: TradingState):
        """
        Analyzes trading state and market data to decide on and place trading orders.
        
        This method processes the current trading state, including market observations and order depths,
        to determine trading actions. It prints details about the trading environment and calculates which
        trades to execute based on an internally defined acceptable price. Orders to buy or sell are generated
        accordingly.
        
        :param state: The current trading state, encapsulating market data and trader-specific information.
        :type state: TradingState
        
        :return: A tuple containing the result (a dictionary mapping products to orders), conversions (the number
                 of conversion operations to perform), and traderData (a string representing the trader's state for
                 the next execution cycle).
        :rtype: tuple
        
        The method prints details about acceptable prices, buy and sell order depths, and any trading actions taken.
        It returns a dictionary of trading orders for different products, a conversions counter, and a string representing
        the trader's state, which will be provided in `TradingState.traderData` in the next execution.
        """
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

				# Orders to be placed on exchange matching engine
        result = {}
        for product in state.order_depths:
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []
            acceptable_price = 10  # Participant should calculate this value
            print("Acceptable price : " + str(acceptable_price))
            print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
    
            if len(order_depth.sell_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                if int(best_ask) < acceptable_price:
                    print("BUY", str(-best_ask_amount) + "x", best_ask)
                    orders.append(Order(product, best_ask, -best_ask_amount))
    
            if len(order_depth.buy_orders) != 0:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                if int(best_bid) > acceptable_price:
                    print("SELL", str(best_bid_amount) + "x", best_bid)
                    orders.append(Order(product, best_bid, -best_bid_amount))
            
            result[product] = orders
    
		    # String value holding Trader state data required. 
				# It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData