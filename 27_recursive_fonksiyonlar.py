# faktoriyel çözümü
# recursive fonksiyonlara güzel bir örnek
# özyinelemeli






def faktoriyel(n):
    if n==0 or n==1:
        return 1
    else:
        return n * faktoriyel(n-1) #5 * 4 * 3 * 2 *1

print(faktoriyel(6))