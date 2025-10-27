print(chr(65))
print(chr(97))
print(chr(90))
print(chr(64))
print(chr(32))
print(chr(27))



print(ord('A'))
print(ord("A")) #python çift tırnağıda destekler
print(ord(' '))
#print(ord(''))

import random
s = ""
for i in range(10): #rastgele 5 harfli string uretelim
    a = random.randint(0,1)
    if a == 0:
        s += chr(random.randint(65,90))
    else :
        s += chr(random.randint(97, 122))
print(s)
