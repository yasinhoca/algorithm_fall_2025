#polymorphism
#çok biçimlilik

class kopek:
    def ses(self):
        print("hav hav")


class kedi:
    def ses(self):
        print("miyav")

class kus:
    def ses(self):
        print("cik cik")

def hayvanSesi(hayvan):
    hayvan.ses()

ko = kopek()
#ko.ses()
ke = kedi()
ku = kus()

hayvanSesi(ke)



