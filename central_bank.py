from subject import Subject


class CentralBank(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self._inflation = 0
        self._cash = 0
        self._tax_last = 0

    def accept(self, visitor):
        visitor.visit(self)

    @property
    def inflation(self):
        return self._inflation

    @inflation.setter
    def inflation(self, value):
        self._inflation = value
        self.notify_inflation()

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, value):
        self._cash = value

    def update(self, visitor):
        self.inflation = visitor.inflation

    def update_new_product(self, subject):
        #zmiana listy produktow
       pass

    #metoda uruchomiana po zmianie w kasie sprzedawcy
    def update_seller_cash(self, subject):
        self._cash += subject.tax
        print("Tax ", subject.tax)
        if self._tax_last == 0:
            self._tax_last = subject.tax
        else:
            if subject.tax - self._tax_last < 0:
                self.inflation += 0.1
            if subject.tax - self._tax_last > 0:
                self.inflation -= 0.1

    def update_buyers_cash(self, subject):
        # zmiana kasy kupujacych
        pass
