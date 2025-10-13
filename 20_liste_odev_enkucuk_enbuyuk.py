import random as r

liste = []

for i in range(10):
    liste.append(r.randint(0,100))

print(liste)

liste.sort();
print(liste)
print("En küçük",liste[0])
print("En büyük",liste[-1])
print("Farkı =", liste[-1]-liste[0])