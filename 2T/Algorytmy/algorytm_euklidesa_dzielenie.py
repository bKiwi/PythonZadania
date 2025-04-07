liczba1 = int(input("podaj liczbe: "))
liczba2 = int(input("podaj liczbe: "))
reszta = 1 
while reszta != 0:
    reszta = liczba1 % liczba2
    liczba1 = liczba2
    liczba2 = reszta
print(liczba1)
#
