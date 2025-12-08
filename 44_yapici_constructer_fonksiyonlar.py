#yapıcı fonksiyonlar
#constructer functions


class cokgen:
    genislik=0
    yukseklik=0

    def __init__(self,yukseklik,genislik): # yapıcı - constructer
        self.yukseklik = yukseklik  #initialize başlangıç değeri
        self.genislik = genislik

    def alan(self):
        return self.genislik*self.yukseklik

dikdortgen = cokgen(15,10)
print(dikdortgen.alan())