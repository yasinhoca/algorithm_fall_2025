import random
liste=[random.randint(0,100) for i in range(10)]
print(liste)

dizi = list(filter(lambda x:x<50 and x%3<2,liste))
print(dizi)

dizi = list(map(lambda x:x/4 if x>25 and x%4==0 else x,liste))
print(dizi)

from functools import reduce

l = [8,0,3,4,1,1,9]

r = reduce(lambda x,y:x if 2<x<5 and y%4<2 else y,l)
print(r)
