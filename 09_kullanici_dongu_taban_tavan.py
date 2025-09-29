taban=int(input("For döngüsü tabanını gir="))
tavan=int(input("For döngüsü tavanını gir="))

for i in range(taban,tavan):
    if i%13==0 and i%17==0:
        print(i,end=" ")

        