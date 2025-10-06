import random as r

s = [] #boş s kümesi

for i in range(20):
    s.append(r.randint(0,100))

print(s)

k = b = 0

for i in s:
    if i>=50:
        b+=1
    else:
        k+=1

print("Küçüklerin sayısı =",k)
print("Büyüklerin sayısı =",b)