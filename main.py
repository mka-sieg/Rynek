from seller import Seller
from buyer import Buyer
from visitor import VisitorProduction, VisitorUpdateSeller, VisitorUpdateBuyer, VisitorUpdateBank
from central_bank import CentralBank
import random as r

#ustawienie wartosci dla sprzedawcow - marza, cena produkcji, kasa
def setup_sellers():
    list_sellers = []
    for i in range(0, 2):
        seller = Seller()
        visit_s = VisitorUpdateSeller(r.randint(1, 10), r.randint(1, 20), r.randint(100, 1000))
        seller.accept(visit_s)
        list_sellers.append(seller)
    return list_sellers

#ustawienie wartosci dla kupujacych - kasa, ile ma kupic produktow
def setup_buyers():
    list_buyers = []
    for i in range(0, 2):
        buyer = Buyer()
        visit_k = VisitorUpdateBuyer(r.randint(1, 4), r.randint(100, 200))
        buyer.accept(visit_k)
        list_buyers.append(buyer)
    return list_buyers


def start():
    bank = CentralBank()
    list_sellers = setup_sellers()
    list_buyers = setup_buyers()

    visitor_p = VisitorProduction()
    #dolaczenie obserwatorow, wszyscy obserwujacy obserwuja wszystkich sprzedawcow, bank obserwuje wszystkich  sprzedawcow
    for seller in list_sellers:
        for buyer in list_buyers:
            seller.attach(buyer)
        seller.attach(bank)
        bank.attach(seller)
    #dolaczenie obserwatorow - bannk obserwuje wszystkich kupujacych, kupujacy obserwuja bank
    for buyer in list_buyers:
        buyer.attach(bank)
        bank.attach(buyer)
    # ustawienie inflacji startowej
    visit_b = VisitorUpdateBank(0.5)
    bank.accept(visit_b)

    for i in range(0, 5):
        #produkcja produktow w sklepie
        for seller in list_sellers:
            seller.accept(visitor_p)

        """ #wyplata pensji i dodanie produktow do listy zakupow
        for buyer in list_buyers:
            visit_k = VisitorUpdateBuyer(r.randint(0, 1), r.randint(0, 100))
            buyer.accept(visit_k)"""

        for seller in list_sellers:
            for buyer in list_buyers:
                if buyer.how_much_to_buy() == 0:
                    seller.detach(buyer)
                # elif buyer.how_much_to_buy() > 0:
                #    seller.attach(buyer)

    for seller in list_sellers:
        print('Seller: ', seller.cash)
    for buyer in list_buyers:
        print(buyer.list_product())
        print('Buyer: ', buyer.cash)

    print('Bank: ', bank.cash)


start()

