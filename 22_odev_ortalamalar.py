import math
import random as r
l = []
for i in range(10):
    l.append(r.randint(0,100))
print(l)




toplam = 0;
for i in l:
    toplam+=i
print("Toplam=",toplam)
o=toplam/len(l)
print("Aritmetik ortalama =",o)


#geo için çarpımları bulalım
carpim = 1
for i in l:
    carpim*=i
print("Çarpımları =",carpim)
print("Geo ort =",math.pow(carpim,(1/10)))

#harmonik için 1/x değerler toplamı
htoplam = 0
for i in l:
    htoplam+=(1/i)
print("Harmonik 1/x toplamları",htoplam)
print("Harmonik ort=",len(l)/htoplam)

#standart sapma
#varyans hesaplama
varyans=0
for i in l:
    varyans+=math.pow((o-i),2)
print("varyans=",varyans)
ssapma= math.sqrt(varyans/(len(l)-1))
print("Standart sapma=",ssapma)

#medyanı bulalım
l.sort()
print(l)
e1 = 5
e2 = 4
print("e1",l[e1])
print("e2",l[e2])
print("Medyan =",(l[e1]+l[e2])/2)