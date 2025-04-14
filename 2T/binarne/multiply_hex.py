def hex_na_dec(znak):
    znaki = "0123456789ABCDEF"
    return znaki.index(znak.upper())

def dec_na_hex(liczba):
    znaki = "0123456789ABCDEF"
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        wynik = znaki[liczba % 16] + wynik
        liczba //= 16
    return wynik

def hex_str_na_dec(tekst):
    wynik = 0
    for znak in tekst:
        wynik = wynik * 16 + hex_na_dec(znak)
    return wynik

def mnozenie_hex(hex1, hex2):
    dec1 = hex_str_na_dec(hex1)
    dec2 = hex_str_na_dec(hex2)
    wynik_dec = dec1 * dec2
    return dec_na_hex(wynik_dec)

hex1 = input("Podaj pierwszą liczbę HEX: ")
hex2 = input("Podaj drugą liczbę HEX: ")

wynik = mnozenie_hex(hex1, hex2)
print(f"Wynik mnożenia {hex1.upper()} × {hex2.upper()} = {wynik}")
