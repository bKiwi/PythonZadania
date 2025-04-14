hex_input = input("Podaj liczbę szesnastkową (HEX): ").upper()

znaki_hex = "0123456789ABCDEF"
wynik = 0
potega = 0

for znak in reversed(hex_input):
    wartosc = znaki_hex.index(znak)
    wynik += wartosc * (16 ** potega)
    potega += 1

print("Postać dziesiętna:", wynik)
