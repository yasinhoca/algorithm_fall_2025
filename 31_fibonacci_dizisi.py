fibo = [0,1]

for i in range(2,20):
    fibo.append(fibo[i-2]+fibo[i-1])

print(fibo)

print("")
print("Altın oran")
for i in range(1,len(fibo)-2):
    ort = fibo[i+1]/fibo[i]
    print(ort,end=" ")

