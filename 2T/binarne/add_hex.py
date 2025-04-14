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

def dodaj_hex(liczba1, liczba2):
    dec1 = 0
    for znak in liczba1:
        dec1 = dec1 * 16 + hex_na_dec(znak)

    dec2 = 0
    for znak in liczba2:
        dec2 = dec2 * 16 + hex_na_dec(znak)

    suma = dec1 + dec2

    return dec_na_hex(suma)

hex1 = input("Podaj pierwszą liczbę HEX (np. 1A): ")
hex2 = input("Podaj drugą liczbę HEX (np. 2F): ")

wynik = dodaj_hex(hex1, hex2)
print(f"Suma {hex1.upper()} + {hex2.upper()} = {wynik}")
