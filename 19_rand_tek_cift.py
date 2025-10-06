import random as r

s = []
for i in range(10):
    s.append(r.randint(0,100))

print(s)


tek = []
cift = []

for i in s:
    if i%2==0:
        cift.append(i)
    else:
        tek.append(i)

print(tek)
print(len(tek))
#teklerin en küçüğünü bulalım
tek.sort()
print(tek)
print("en küçük tek =",tek[0])

print(cift)
print(len(cift))
#en büyük çifti bulalım
cift.sort()
print(cift)
print("En büyük çift =",cift[-1])