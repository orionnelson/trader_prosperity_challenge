class ConversionObservation:
    """
    Represents a set of market and environmental observations relevant to trading decisions.
    
    This class encapsulates both market-related data, such as bid and ask prices, as well as environmental
    factors like sunlight and humidity, which could influence the trading strategy for certain products.

    :param bidPrice: The current highest price a buyer is willing to pay for a product.
    :type bidPrice: float
    :param askPrice: The current lowest price a seller is willing to accept for a product.
    :type askPrice: float
    :param transportFees: Costs associated with transporting goods from the seller to the buyer.
    :type transportFees: float
    :param exportTariff: Taxes imposed on goods leaving a country.
    :type exportTariff: float
    :param importTariff: Taxes imposed on goods entering a country.
    :type importTariff: float
    :param sunlight: The amount of sunlight, potentially influencing the quality or availability of certain products.
    :type sunlight: float
    :param humidity: The level of humidity, which could affect the condition or preservation of products.
    :type humidity: float
    """
    def __init__(self, bidPrice: float, askPrice: float, transportFees: float, exportTariff: float, importTariff: float, sunlight: float, humidity: float):
        self.bidPrice = bidPrice
        self.askPrice = askPrice
        self.transportFees = transportFees
        self.exportTariff = exportTariff
        self.importTariff = importTariff
        self.sunlight = sunlight
        self.humidity = humidity