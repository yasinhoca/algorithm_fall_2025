#0 ile yüz arasında rastgele sayılardan 50 eleman oluşan
#bir dizide 50den küçükleri bir diziye
#50den büyükleri başka bir diziye filtreyelim

import random

dizi = [random.randint(0,100) for i in range(10)]
print(dizi)

kucuk = list(filter(lambda x:x<50,dizi))
print(kucuk)

buyuk = list(filter(lambda x:x>=50,dizi))
print(buyuk)

#elli ile seksen arasındakileri bir diziye atmak istersem

aralik = list(filter(lambda x:x>=50 and x<80,dizi))
print(aralik)