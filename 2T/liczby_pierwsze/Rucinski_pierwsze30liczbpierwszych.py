#liczby pierwsze mniejsze niz 100
liczbyPierwsze = []

def pierwsze30():
    ilosc = 0
    while len(liczbyPierwsze) != 30:
        if czy_pierwsza(ilosc) == True and ilosc not in liczbyPierwsze:
            liczbyPierwsze.append(ilosc)
        else:
            ilosc+=1
    print(liczbyPierwsze)


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
print(pierwsze30())
            

        
        