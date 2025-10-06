#listeler (diziler)
#her öğrencinin vize notunu tek tek değişkende mi tutmalıyız?
#listeler seri halinde bunları tutmamızı sağlar
ogrenciler = [37,67,90,12,45]

print(ogrenciler[0]) #37 yazar
print(ogrenciler[1]) #67 yazar
print(ogrenciler[4]) #45 yazar
# print(ogrenciler[5]) #taşma hatası verir 5. indis yok

meyveler = ["elma","armut","çilek","erik","karpuz"]
print(meyveler[3]) #erik
print(meyveler[2]) #çilek

print(meyveler[0][0]) #e
print(meyveler[4][3]) #p

for i in meyveler: #meyveler listesindek, her meyve döngüde i'ye atanır
    print(i)

for i in range(len(meyveler)):
    print(meyveler[i])