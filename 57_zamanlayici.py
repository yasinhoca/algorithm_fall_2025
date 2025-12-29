#Timer - Zamanlayıcı

import time
from tkinter import *

#for i in range(30,0,-1):
   # print(i)
   # time.sleep(1) # 1000 ms = 1 sn   --> sleep komutu saniye cinsinden
                    # 0.1 = 100 ms

pencere = Tk()
pencere.geometry("300x300")

i=0
def yaz():
    global i
    i+=1
    #l['text']=str(i)   labelin text özelliğini değiştirme
    l.configure(text=str(i))  #label özelliğini değiştirmenin 2. yolu
    pencere.after(1000,yaz)

l = Label(text="SAYAC",fg="yellow",bg="blue",font="verdana 22 bold")
l.place(x=100,y=100)

yaz()

pencere.mainloop()


