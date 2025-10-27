a = 10 #global

def fonk():
    a=5 #local değişkendir yukarıdaki a ile farklı ram adreslerinde saklanır
    print(a)

fonk()
print(a)

b = 20 #global

def ikiKati():
    global b
    b=5
    b *=2
    print(b)

ikiKati()
print(b)