n = int(input("Podaj liczbę dziesiętną: "))

wynik = ''
while n > 0:
    wynik = str(n % 2) + wynik
    n = n // 2

print("Postać binarna:", wynik or '0')
