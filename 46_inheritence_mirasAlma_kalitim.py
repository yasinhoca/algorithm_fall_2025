#inheritence - mirasAlma- kalıtım
class universite:
    universite_adi="Necmettin Erbakan Üniversitesi"
    universite_sehir="Konya"
    rektor="Cem Zorlu"
    universite_ogrenciSayisi=35000



class fakulte(universite): #fakulte sınıfı babası olan universiteden miras alır
    fakulte_adi="UBF"
    dekan = "Mustafa Kocaoğlu"
    fakulte_ogrenciSayisi=2000

class bolum(fakulte):
    bolum_adi = "YBS"
    baskan = "Buluthan Çetintaş"
    bolum_ogrenciSayisi=400

ubf = fakulte()
print(ubf.universite_adi) #babasından (super class universite)
print(ubf.fakulte_adi) #kendinden

ybs = bolum()
print(ybs.rektor) #dededen (universite)
print(ybs.dekan) #babadan (fakulte)
print(ybs.baskan) #kendinden
