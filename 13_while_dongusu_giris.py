isim = input("İsminizi giriniz : ")
sayac = 0

while sayac<20:
    print(sayac,". ",isim)
    sayac += 1


##Kullanıcıdan 20 ile 30 arasında bir sayı girmesini isteyelim
while True: #burada 1<2 gibi bir ifade de sonsuz döngü oluşturur çünkü 1 her zaman 2 den küçüktür yani truedur
    s = int(input("20-30 arası bir sayı giriniz:"))
    if s>=20 and s<=30:
        break
    else:
        print("Lütfen istenen aralıkta bir sayı giriniz!")