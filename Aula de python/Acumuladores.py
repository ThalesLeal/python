## calcular  a media  de 10  numeros inteiros##
n = 1
soma =0
while n <=10:
    x = int(input("Digite o %d número: " %n))
    soma = soma + x
    n = n + 1
    print("Media:   %5.2f" %(soma/10))