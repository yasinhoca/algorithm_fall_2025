#amacımız kullanıcıdan aldığımız bir ismin
#aynısını rastgele harf üreterek buldurmaya çalışmak
#fonksiyon kullanacağız
import  random

def stringBul(s):
    uzunluk = len(s)
    rs = ""
    for i in range(uzunluk):
        rs += chr(random.randint(65,90))
    return rs

s = input("İsminizi giriniz:")
sayac = 0

while True:
    r = stringBul(s)
    sayac += 1
    print(sayac,".deneme",r)
    if r==s:
        break
