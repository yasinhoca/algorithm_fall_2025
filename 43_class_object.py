# class - object
# sınıf - nesne kavramları

ad = "Ali"
soyad = "Altan"

class ogrenci:
    #global ad  #başına global yazarak sınıf içinde de kullanılabilir
    numara = 534
    ad = "Volkan" #local
    soyad = "Bal" #local
    email = "v@v.com"
    v = 64
    f = 100

    def yazdir(self):
        print(self.numara)
        print(self.ad)
        print(self.soyad)
        print(self.email)

    def ortalama(self,v,f):
        #return self.v*0.5+self.f*0.5 #localdeki v ve f değişkenleri için
        return v*0.5+f*0.5


nesne = ogrenci()
print(nesne.ad)
print(nesne.soyad)
#nesne.yazdir()
print(nesne.ortalama(80,100))

nesne2 = ogrenci()
nesne2.ad="Samet"
nesne2.soyad="Gündoğar"
nesne2.numara=456
nesne2.email="s@s.com"
nesne2.yazdir()
