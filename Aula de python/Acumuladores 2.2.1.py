## Calcule o fatorial  de um numero inteiro n ##

i = 1
fat = 1
n = int(input("Digite n: "))
while i <=n:
    fat = fat * i
    i = i + 1
print("fat(%d) = %d" %(n,fat))
