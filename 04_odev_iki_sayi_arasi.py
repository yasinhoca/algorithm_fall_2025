#İki sayı arasındaki fark 20den büyükse ve çiftse true
#değilse false yazalım

a = int(input("a sayısı ="))
b = int(input("b sayısı ="))
fark = abs(a-b)



if fark>20 and fark%2==0:
    print(True)
else:
    print(False)

