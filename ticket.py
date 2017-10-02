class Ticket:
    """The class Ticket holds the price of each ticket.
    Attributes to a ticket can be easily added here
    """
    def __init__(self, price):
        self.price = price

    def get_price(self):
        """Returns the price of a ticket
        """
        return self.price
