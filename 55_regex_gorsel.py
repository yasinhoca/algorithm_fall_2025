import tkinter as tk
import re

def bul():
    yazi = t.get("1.0","end-1c") #büyük text alanındaki tekerlemeyi alıyoruz
    iz = p.get() #patterni alıyoruz
    #regex ile buluyoruz
    a = re.findall(iz,yazi)
    print(a)
    adet = len(a)
    #labele yazdıralım
    l['text'] = str(adet) + " pattern bulundu"

pencere = tk.Tk()
pencere.geometry("300x350")

t = tk.Text(width=15,height=5,font="ariel 22 bold")
t.place(x=20,y=10)

p = tk.Entry(width=15,font="ariel 22 bold")
p.place(x=20,y=200)

b = tk.Button(text="BUL",font="ariel 18 bold",command=bul)
b.place(x=20,y=250)

l = tk.Label(text="Sonuç",font="ariel 18 bold")
l.place(x=20,y=300)


pencere.mainloop()