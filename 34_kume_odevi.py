import random as burhan

def diziUret():
    dizi=[]
    for i in range(10):
        dizi.append(burhan.randint(0,10))
    return dizi


a = diziUret()
a.sort()
print(a)
b = diziUret()
b.sort()
print(b)

seta = set(a)
print(seta)
setb = set(b)
print(setb)

print(seta.difference(setb))
print(seta.union(setb))
print(seta.intersection(setb))