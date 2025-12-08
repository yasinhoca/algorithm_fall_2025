#Encapsulaion - Kapsulleme

class urun:
    def __init__(self):
        self.fiyat = 1000
        #tckimlik_no=22222222

    def setFiyat(self,f):
        self.fiyat = f

    def getFiyat(self):
        return self.fiyat

nesne = urun()
nesne.setFiyat(900)
print(nesne.getFiyat())