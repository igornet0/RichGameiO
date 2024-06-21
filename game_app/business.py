class Business:
    """
    Класс бизнес
    """

    def __init__(self, name: str, profit: float, taxes: float):
        self.name = name
        self.profit = profit
        self.taxes = taxes

    def get_clear_profit(self):
        return self.profit - self.taxes

    def __str__(self):
        return f'{self.name} {self.profit} {self.taxes} {self.get_clear_profit()}'