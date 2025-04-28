def NWD(a,b):
    while a != b:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
    NWD = a
    return NWD
licznik1 = int(input("podaj licznik pierwszego ulamka: "))
mianownik1 = int(input("podaj mianownik pierwszego ulamka: "))

licznik2 = int(input("podaj licznik drugiego ulamka: "))
mianownik2 = int(input("podaj mianownik drugiego ulamka: "))
nwd = NWD(mianownik1, mianownik2)
nww = (mianownik1 * mianownik2) // nwd
licznik_koncowy = licznik1 * licznik2
mianownik_koncowy = mianownik1 * mianownik2
dzielnik = NWD(licznik_koncowy, mianownik_koncowy)
licznik = licznik_koncowy // dzielnik
mianownik = mianownik_koncowy // dzielnik
print(licznik,"/", mianownik)
