taban = int(input("Taban="))
tavan = int(input("Tavan="))
bolen1 = int(input("Bölen 1="))
bolen2 = int(input("Bölen 2="))

for i in range(taban,tavan):
    if i%bolen1==0 or i%bolen2==0:
        print(i,end=" ")