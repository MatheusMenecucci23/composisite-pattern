from conjunto import elements


class objeto(elements):
    def __init__(self, price):
        self.price = price

    def calulate_price(self):
        return self.price


    def showContent(self):
        return f"Objeto com preço: R${self.price:.2f}"

