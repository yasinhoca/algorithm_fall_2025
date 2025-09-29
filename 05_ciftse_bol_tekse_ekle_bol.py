#girilen sayı çiftse 2 ye böl
#tek ise bir ekle ikiye böl
a = int(input("Bir sayı giriniz ="))
if a%2==0:
    a/=2 #aslında a=a/2 ye eşittir
    print(a)
else:
    a=(a+1)/2
    print(a)