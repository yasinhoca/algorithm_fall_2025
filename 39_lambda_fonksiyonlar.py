#anonim ve lambda fonksiyonlar

def topla(a,b):
    return a+b

#yukarıda iki sayıyı toplayan fonksiyonun lambda tanımı
k = lambda x,y:x+y

print(k(3,4))

dizi = [3,2,0,2,5,7,8,4,9]
print(dizi)

cift = list(filter(lambda x:x%2==0,dizi))
print(cift)

tek = list(filter(lambda x:x%2==1,dizi))
print(tek)

b = list(filter(lambda x:x>1 and x<5,dizi))
print(b)

c = list(filter(lambda x:x>10,dizi))
print(c)