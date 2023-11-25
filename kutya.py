class Kutya:
    def __init__(self, nev, kor, faj):
        self.nev = nev
        self.kor = kor
        self.faj = faj

    def emberi_evekben(self):
        if self.faj.lower() == 'tacskó':
            emberi_kor = self.kor * 8
        else:
            emberi_kor = self.kor * 7
        return emberi_kor

# Példa használat
kutya1 = Kutya("Bodri", 3, "Golden Retriever")
kutya2 = Kutya("Csöpi", 2, "Tacskó")
kutya3 = Kutya("Furkesz", 4, "Tacskó")

print(f"{kutya1.nev} {kutya1.kor} éves, emberi években: {kutya1.emberi_evekben()}")
print(f"{kutya2.nev} {kutya2.kor} éves, emberi években: {kutya2.emberi_evekben()}")
print(f"{kutya3.nev} {kutya3.kor} éves, emberi években: {kutya3.emberi_evekben()}")