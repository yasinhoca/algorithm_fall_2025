import random as r

rastgele = r.randint(0,100)
sayac = 0
tahmin = int(input("Bir tahminde bulun :"))
sayac+=1



while True:
    if tahmin==rastgele:
        print("Tebrikler!",sayac,". denemede bildiniz!")
        break
    elif tahmin>rastgele:
        print("Daha küçük tahmin et!")
        print(sayac,". deneme")
    elif tahmin<rastgele:
        print("Daha büyük tahmin et!")
        print(sayac, ". deneme")
    tahmin = int(input("Bir tahminde bulun : "))
    sayac+=1