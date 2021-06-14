from subject import Subject


class Seller(Subject):
    def __init__(self,  name=''):
        Subject.__init__(self)
        self._cash = 0
        self._old_products_list = []
        self._new_product = 0
        self._margin = 0
        self._tax = 0
        self._price_production = 0

    @property
    def new_product(self):
        return self._new_product

    @new_product.setter
    def new_product(self, value):
        self._new_product = value
        self.notify_new_product()

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value
        self.notify_seller_cash()

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        self._tax = value

    def accept(self, visitor):
        visitor.visit(self)

    #dodanie pieniedzy po sprzedazy
    def sold_product(self, visitor):
        self.cash = self._cash + int(visitor.num) - self._tax
        print(self, "Sold ", visitor.num)

    #nowy produkt
    def production_product(self, visitor):
        price = self._margin + self._tax + self._price_production
        print(self, "Update by ", visitor)
        print(self, "Added ", price)
        if self.new_product != 0:
            self._old_products_list.append(self.new_product)
        self.new_product = price

    #aktualizacja wartosci
    def update(self, visitor):
        self._price_production += visitor.price_production
        self._margin += visitor.margin
        self.cash += visitor.cash

    def update_inflation(self, subject):
        self._tax = self._margin * subject.inflation


class Seller1(Seller):
    pass

