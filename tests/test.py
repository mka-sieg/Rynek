#test obserwatora inflacji
def test_viewer_inflation():
    from seller import Seller
    from central_bank import CentralBank

    seller = Seller()
    seller._margin = 1
    bank = CentralBank()
    bank.attach(seller)
    bank.inflation = 10
    assert seller._tax == 10

#test obserwatora nowego produktu
def test_viewer_product():
    from seller import Seller
    from buyer import Buyer

    seller = Seller()
    buyer = Buyer()
    buyer.cash = 10
    buyer._how_much_to_buy = 1
    seller.attach(buyer)
    seller.new_product = 10
    assert seller.cash == 10

#test visitora zmiana przy sprzedarzy
def test_visitor_sold():
    from seller import Seller
    from visitor import VisitorSold

    seller = Seller()
    visitor3 = VisitorSold(10)

    seller.accept(visitor3)
    assert seller.cash == 10

#test visitora zmiana przy produkcji
def test_visitor_prod():
    from seller import Seller
    from visitor import VisitorProduction, VisitorUpdateSeller
    from central_bank import CentralBank
    bank = CentralBank()

    visitor2 = VisitorProduction()
    seller = Seller()
    visit_s = VisitorUpdateSeller(10, 20, 0)
    seller.accept(visit_s)

    bank.attach(seller)
    bank.inflation = 0.5
    seller.accept(visitor2)

    assert seller.new_product == 40
