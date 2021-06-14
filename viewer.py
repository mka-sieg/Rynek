from buyer import Kupujacy
class Inflacja_Viewer:
    """updates the Hewviewer"""

    def update(self, subject):
        print('Inflacja_Viewer:  changed to', subject.inflacja)

class Kasa_Viewer:
    """updates the Hewviewer"""

    def update(self, subject):
        print('Kasa_Viewer:  changed to', subject.kasa)

class Product_Viewer():
    """updates the Hewviewer"""

    def update(self, subject):
        print('Product_Viewer:  changed to', subject.lista_produktow)

class Podatek_Viewer:
    """updates the Hewviewer"""

    def update(self, subject):
        print('Podatek_Viewer:  changed to', subject.podatek)