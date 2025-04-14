import random
liczba = random.randint(1, 10)
zgadniecie = 0
while zgadniecie != liczba:
    zgadniecie = int(input("zgadnij liczbe od 1 do 10: "))

print("zgadles liczbe!")