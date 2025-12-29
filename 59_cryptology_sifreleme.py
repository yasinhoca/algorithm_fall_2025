from tkinter import *

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
ters = alfabe[::-1]

def sezar():
    global alfabe
    m = metin.get()
    km = int(kaydirma.get())
    sifreli = ""
    indis = 0
    for j in range(len(m)):
        for i in range(len(alfabe)):
            if m[j]==alfabe[i]:
                indis = i
        sifreli += alfabe[(indis+km)%29]
    sonuc['text'] = sifreli

def atbash():
    global alfabe,ters
    m = metin.get()
    sifreli = ""
    indis = 0
    for j in range(len(m)):
        for i in range(len(alfabe)):
            if m[j]==alfabe[i]:
                indis = i
        sifreli += ters[indis]
    sonuc['text'] = sifreli


pencere = Tk()
pencere.geometry("300x300")

l1 = Label(text="Şifrelenecek metin",font="verdana 14 bold")
l1.place(x=10,y=10)
metin = Entry(width=15,font="verdana 14 bold")
metin.place(x=10,y=40)

l2 = Label(text="Kaydırma miktarı",font="verdana 14 bold")
l2.place(x=10,y=70)
kaydirma = Entry(width=5,font="verdana 14 bold")
kaydirma.place(x=10,y=110)

b = Button(text="SEZAR",font="verdana 14 bold",bg="navy",fg="yellow",command=sezar)
b.place(x=10,y=150)

b2 = Button(text="ATBASH",font="verdana 14 bold",bg="navy",fg="yellow",command=atbash)
b2.place(x=120,y=150)

sonuc = Label(text="SONUÇ",font="verdana 14 bold")
sonuc.place(x=10,y=210)
pencere.mainloop()