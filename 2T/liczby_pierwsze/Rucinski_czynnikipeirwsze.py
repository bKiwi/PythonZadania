liczba_calkowita = int(input("podaj liczbe calkowita: "))
liczbyPierwsze = []

def sprawdz_czynniki(calkowita):
    ilosc_czynnikow = 0
    for x in liczbyPierwsze:
        if calkowita%x == 0:
            ilosc_czynnikow += 1
    print("liczba ", calkowita, " posiada ", ilosc_czynnikow, "czynnikow pierwszych")
            
def sprawdz_zakres(ilosc):
    for i in range(1, ilosc):
        if czy_pierwsza(i) == True:
            liczbyPierwsze.append(i)
    sprawdz_czynniki(liczba_calkowita)

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            return False
        return True
    
    
sprawdz_zakres(liczba_calkowita)
    

            

        
        