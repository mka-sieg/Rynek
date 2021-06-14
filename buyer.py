from subject import Subject
from visitor import VisitorSold


class Buyer(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self._cash = 100
        self._list_product = []
        self._how_much_to_buy = 0

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value
        self.notify_buyers_cash()

    def list_product(self):
        return self._list_product

    def how_much_to_buy(self):
        return self._how_much_to_buy

    def accept(self, visitor):
        visitor.visit(self)

    def products_buy(self, num):
        self._cash -= num
        self._how_much_to_buy -= 1
        self._list_product.append(num)
        print(self, "Sold ", num)

    # aktualizacja wartosci
    def update(self, visitor):
        self._how_much_to_buy += visitor.how_much_to_buy
        self.cash += visitor.cash
        print("Buyer: ", self.cash, " ", self._how_much_to_buy)

    #metoda uruchomiana po pojawieniu sie nowego produktu u sprzedawcy
    def update_new_product(self, subject):
        if self._how_much_to_buy > 0:
            if subject._new_product != 0:
                product = subject.new_product
                if product <= self.cash / self._how_much_to_buy:
                    subject._new_product = 0
                    visitor_s = VisitorSold(product)
                    subject.accept(visitor_s)
                    self.products_buy(product)
                else:
                    product = min(subject.old_products_list)
                    if min(subject.old_products_list) <= self.cash / self._how_much_to_buy:
                        subject.old_products_list.remove(product)
                        visitor_s = VisitorSold(product)
                        subject.accept(visitor_s)
                        self.products_buy(product)
        print(self._list_product)

    def update_seller_cash(self, subject):
        #zmiana kasy sprzedawcy
        pass

    def update_inflation(self, subject):
        #zmiana inflacji
        pass


class Buyer1(Buyer): pass
