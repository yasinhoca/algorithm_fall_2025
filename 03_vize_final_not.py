v = int(input("Vize ="))
f = int(input("Final ="))
ort = (v+f)/2
print("Ortalamanız =",ort)
if ort>=90 and ort<=100:
    print("AA")
elif ort>=85 and ort<90:
    print("BA")
elif ort>=75 and ort<85:
    print("BB")
elif ort>=70 and ort<75:
    print("CB")
elif ort>=60 and ort<70:
    print("CC")
elif ort>=55 and ort<60:
    print("DC")
    print("Şartlı geçer")
else:
    print("FF")