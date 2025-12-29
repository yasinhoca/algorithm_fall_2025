# Lambda ve Regex kullanımı
import re

dizi = ["algoritma","ders","programcılık","akış şemaları","diyagram","python","java"]

a = list(filter(lambda x:re.findall("[gro]{3}",x),dizi))
print(a)

s = "Oraya gitme demedim mi sana, " \
    "seni yalnız ben tanırım demedim mi? " \
    "Demedim mi bu yokluk yurdunda hayat çeşmesi ben'im? " \
    "Bir gün kızsan bana, alsan başını, yüz bin yıllık yere gitsen," \
    "dönüp kavuşacağın yer ben'im demedim mi? " \
    "Demedim mi şu görünene razı olma, " \
    "demedim mi sana yaraşır otağı kuran ben'im asıl," \
    "onu süsleyen, bezeyen ben'im demedim mi?"

d = re.split("[\s]",s) #yukarıdaki stringi split ile boşluklardan kırıyoruz, kelime kelime ayırıyoruz
print(d)

l = list(filter(lambda x: re.findall("[im]{2}",x),d))
print(l)


