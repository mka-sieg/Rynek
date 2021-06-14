
class Visitor:
    def __str__(self):
        return self.__class__.__name__

#Visitor po sprzedarzy
class VisitorSold(Visitor):
    def __init__(self, num):
        self._num = num

    @property
    def num(self):
        return self._num

    @num.setter
    def margin(self, value):
        self._margin = value

    def visit(self, crop):
        crop.sold_product(self)

#Visitor do produkcji
class VisitorProduction(Visitor):

    def visit(self, crop):
        crop.production_product(self)

#Visitor zmiana wartosci sprzedawcy
class VisitorUpdateSeller(Visitor):

    def __init__(self, price_production=0, margin=0, cash=0):
        self._price_production = price_production
        self._margin = margin
        self._cash = cash

    @property
    def price_production(self):
        return self._price_production

    @price_production.setter
    def price_production(self, value):
        self._cash = value

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = value

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value

    def visit(self, crop):
        crop.update(self)

#Visitor zmiana wartosci kupujacego
class VisitorUpdateBuyer(Visitor):

    def __init__(self, how_much_to_buy=0, cash=0):
        self._how_much_to_buy = how_much_to_buy
        self._cash = cash

    @property
    def how_much_to_buy(self):
        return self._how_much_to_buy

    @how_much_to_buy.setter
    def how_much_to_buy(self, value):
        self._how_much_to_buy = value

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value

    def visit(self, crop):
        crop.update(self)

#Visitor zmiana wartosci banku
class VisitorUpdateBank(Visitor):

    def __init__(self, inflation):
        self._inflation = inflation

    @property
    def inflation(self):
        return self._inflation

    @inflation.setter
    def inflation(self, value):
        self._inflation = value

    def visit(self, crop):
        crop.update(self)
