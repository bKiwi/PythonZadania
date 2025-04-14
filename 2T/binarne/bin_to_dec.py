binarna = input("Podaj liczbę binarną: ")

potega = 0
dziesietna = 0

for cyfra in reversed(binarna):
    dziesietna += int(cyfra) * (2 ** potega)
    potega += 1

print("Postać dziesiętna:", dziesietna)
