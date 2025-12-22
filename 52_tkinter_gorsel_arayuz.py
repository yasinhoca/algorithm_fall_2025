#GUI graphical user interface
# python' da tkinter kütüphanesi ile yapılır

import tkinter as tk

pencere = tk.Tk()
pencere.title("İlk GUI penceresi")
pencere.geometry("500x500+250+70")
#width , height, x, y

etiket = tk.Label(text="tkinter ilk componentimiz",font="Verdana 22 bold",bg="navy",fg="yellow")
etiket.pack()

etiket2 = tk.Label(text="ikinci etiket",font="Ariel 22 bold",bg="blue",fg="yellow")
etiket2.place(x = 250, y = 250)
#pack() sıra ile componentleri yerleştirir
#grid()
#place()

pencere.mainloop()

pencere2 = tk.Tk()

etiket3 = tk.Label(text="Bende grid ile yerleştim",font="Arial 22 bold")
etiket3.grid(row=0,column=0)
etiket4 = tk.Label(text="grid ile yerleştim",font="Arial 22 bold")
etiket4.grid(row=1,column=1)

etiket5 = tk.Label(text="Üçe üç hücresindeyim",font="Arial 22 bold")
etiket5.grid(row=3,column=3)

pencere2.mainloop()