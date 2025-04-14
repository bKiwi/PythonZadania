liczba = int(input("Podaj liczbę dziesiętną: "))

znaki_hex = "0123456789ABCDEF"
wynik = ""

while liczba > 0:
    reszta = liczba % 16
    wynik = znaki_hex[reszta] + wynik
    liczba = liczba // 16

print("Postać szesnastkowa (HEX):", wynik or "0")
