##calcular o fatorinal do numero n ##

i = 1
fat = 1
num = int(input("Digite o numero"))
while i <= num:
    fat = fat * i
    i = i + 1
print("fat(%d) = %d" %(num,fat))