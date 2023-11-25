class Szoba:
    def __init__(self, szobaszam, foglalt=False, ar=0, extrak=None, tipus=""):
        self.szobaszam = szobaszam
        self.foglalt = foglalt
        self.ar = ar
        self.extrak = extrak if extrak is not None else []
        self.tipus = tipus  # Szoba típusa (egyágyas, kétágyas, lakosztály)

class Szalloda:
    def __init__(self):
        self.szobak = []

    def adatfeltolto(self):
        # Példa adatfeltöltés
        self.szobak.append(Szoba(101, False, 50, ["WIFI", "Reggeli"], "egyágyas"))
        self.szobak.append(Szoba(102, True, 70, ["Reggeli"], "kétágyas"))
        self.szobak.append(Szoba(201, False, 60, ["WIFI"], "lakosztály"))
        # További szobák hozzáadása...

    def foglalas_lekerdezes(self, szoba_tipus=""):
        # Szabad szobák lekérdezése típus alapján
        szabad_szobak = [szoba.szobaszam for szoba in self.szobak
                         if not szoba.foglalt and (szoba_tipus == "" or szoba.tipus.lower() == szoba_tipus.lower())]
        return szabad_szobak

    def arak_lekerdezes(self, szoba_tipus=""):
        # Szobaárak lekérdezése típus alapján
        arak = {szoba.szobaszam: szoba.ar for szoba in self.szobak
                if szoba_tipus == "" or szoba.tipus.lower() == szoba_tipus.lower()}
        return arak

    def foglalas(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and not szoba.foglalt:
                szoba.foglalt = True
                return f"A(z) {szobaszam} szoba sikeresen foglalva."
        return "A foglalás nem lehetséges. A szoba már foglalt vagy nem létezik."


def menu():
    print("1. Foglalás")
    print("2. Szabad szobák lekérdezése")
    print("3. Szobaárak lekérdezése")
    print("0. Kilépés")


if __name__ == "__main__":
    hotel = Szalloda()
    hotel.adatfeltolto()

    while True:
        menu()
        valasztas = input("Válasszon egy menüpontot (0-3): ")

        if valasztas == "0":
            break
        elif valasztas == "1":
            szobaszam = int(input("Adja meg a foglalni kívánt szoba számát: "))
            print(hotel.foglalas(szobaszam))
        elif valasztas == "2":
            szoba_tipus = input("Adja meg a keresett szoba típusát (opcionális, üresen hagyható): ")
            szabad_szobak = hotel.foglalas_lekerdezes(szoba_tipus)
            print(f"Elérhető szobák: {szabad_szobak}")
        elif valasztas == "3":
            szoba_tipus = input("Adja meg a keresett szoba típusát (opcionális, üresen hagyható): ")
            arak = hotel.arak_lekerdezes(szoba_tipus)
            print(f"Szobaárak: {arak}")
        else:
            print("Érvénytelen választás. Kérem, válasszon 0-3 közötti értéket.")
