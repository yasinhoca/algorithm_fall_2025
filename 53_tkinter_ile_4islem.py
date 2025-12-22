import tkinter as tk

def topla():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc['text'] = str(s1+s2)

def cikar():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc['text'] = str(s1-s2)

def carp():
    s1 = int(sayi1.get())
    s2 = int(sayi2.get())
    sonuc['text'] = str(s1*s2)

def bol():
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc['text'] = str(s1/s2)




pencere = tk.Tk()
pencere.geometry("300x300")

sayi1 = tk.Entry(width=5,font="verdana 22 bold")
sayi1.place(x=20,y=20)

sayi2 = tk.Entry(width=5,font="verdana 22 bold")
sayi2.place(x=150,y=20)

sonuc = tk.Label(text="sonuc",bg="blue")
sonuc['font'] = "verdana 22 bold" #label özellikleri sonradan da değiştirilebilir
sonuc['fg'] = "#FFAA00"
sonuc.place(x=100,y=85)

btopla=tk.Button(text="+",font="verdana 22 bold",bg="white",command=topla)
btopla.place(x=20,y=150)

bcikar=tk.Button(text="-",font="verdana 22 bold",bg="white",command=cikar)
bcikar.place(x=90,y=150)

bcarp=tk.Button(text="*",font="verdana 22 bold",bg="white",command=carp)
bcarp.place(x=160,y=150)

bbol=tk.Button(text="/",font="verdana 22 bold",bg="white",command=bol)
bbol.place(x=230,y=150)

pencere.mainloop()