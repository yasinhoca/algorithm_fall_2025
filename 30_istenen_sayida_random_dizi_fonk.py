import random as r

def diziUret(taban,tavan,adet):
    dizi = []
    for i in range(adet):
        dizi.append(r.randint(taban,tavan))
    return dizi

taban = int(input("Taban gir:"))
tavan = int(input("Tavan gir:"))
adet = int(input("Adet gir:"))

dizi = diziUret(taban,tavan,adet)
print(dizi)

