class Item:

    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit

    def get_price(self):
        return self.price