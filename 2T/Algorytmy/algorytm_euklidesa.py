liczba1 = int(input("podaj liczbe: "))
liczba2 = int(input("podaj liczbe: "))

while liczba1 != liczba2:
    if liczba1 > liczba2:
        liczba1 -= liczba2
    else:
        liczba2 -= liczba1
        
print(liczba1)    
