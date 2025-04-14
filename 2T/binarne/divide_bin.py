def bin_na_dec(bin_str):
    wynik = 0
    for znak in bin_str:
        wynik = wynik * 2 + int(znak)
    return wynik

def dec_na_bin(liczba):
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba //= 2
    return wynik

def dzielenie_bin(bin1, bin2):
    dec1 = bin_na_dec(bin1)
    dec2 = bin_na_dec(bin2)

    if dec2 == 0:
        return "Błąd: dzielenie przez zero!"

    wynik_dec = dec1 // dec2

    return dec_na_bin(wynik_dec)

bin1 = input("Podaj pierwszą liczbę binarną (np. 1010): ")
bin2 = input("Podaj drugą liczbę binarną (np. 10): ")

wynik = dzielenie_bin(bin1, bin2)
print(f"Wynik dzielenia {bin1} ÷ {bin2} = {wynik}")
