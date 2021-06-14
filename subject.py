class Subject:

    def __init__(self):
        self._observers = []

    def notify_new_product(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.update_new_product(self)

    def notify_seller_cash(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.update_seller_cash(self)

    def notify_buyers_cash(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.update_buyers_cash(self)

    def notify_inflation(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.update_inflation(self)

    def attach(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):

        try:
            self._observers.remove(observer)
        except ValueError:
            pass
