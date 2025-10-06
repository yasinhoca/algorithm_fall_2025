#Kullanıcıdan taban ve tavan sayıları alınız, bu sayı aralığında tek sayıların adeti, toplamı ve ortalamasını buldurunuz?

baslangic = int(input("Başlangıç :"))
bitis = int(input("Bitiş :"))

adet = toplam = 0
ort = 0


while baslangic<bitis:
    if baslangic % 2 == 1:
        adet+=1
        toplam+=baslangic
    baslangic+=1

print("Tek sayı adeti",adet)
print("Tek sayılar toplamı",toplam)
ort = toplam/adet
print("Ortalaması",ort)

