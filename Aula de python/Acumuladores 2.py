##calcule o fatorial de 10##

n = 1
fat = 1
while n <= 10:
    x = int(input("Digite o %d número: " %n))
    fat = fat + x
    n = n + 1
    print("Media:   %5.2f" %(fat*10))