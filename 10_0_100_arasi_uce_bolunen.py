adet = toplam = ortalama = 0

for i in range(100):
    if i%3==0:
        adet+=1
        toplam+=i



print("0 ve 100 arasında 3'e tam bölünen",adet," sayı vardır")
print("Bu sayıların toplamı = ",toplam)

ortalama = toplam/adet
print("Bu sayıların ortalaması =",ortalama)