a = input("Podaj pierwszą liczbę binarną: ")
b = input("Podaj drugą liczbę binarną: ")

max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

wynik = ""
przeniesienie = 0

for i in range(max_len - 1, -1, -1):
    bit1 = int(a[i])
    bit2 = int(b[i])
    
    suma = bit1 + bit2 + przeniesienie
    wynik = str(suma % 2) + wynik
    przeniesienie = suma // 2

if przeniesienie:
    wynik = "1" + wynik

print("Suma binarna:", wynik)
