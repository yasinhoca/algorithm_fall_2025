import random as r

liste=[]

for i in range(1000):
    liste.append(r.randint(0,1000))

print(liste)

adet = toplam = 0
liste222 = []

for i in liste:
    if i%222==0:
        liste222.append(i)
        adet+=1
        toplam+=i

print("222'e bölünen ",adet," sayı bulundu")
print(liste222)
print("Bunların toplamı =",toplam)
print("Ortalama =",toplam/adet)