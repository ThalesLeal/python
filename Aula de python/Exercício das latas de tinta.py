'''
Faça um programa para loja de tintas.O programa deverá pedir
o tamanho em metros quadrados de area a ser pintada.Considere que
a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros,que custam R$80,00.
Informe ao usuarioa quantidade  de latas de tintas a serem compradas
e o preço total
'''
metros = int(input("Metros:  "))
if metros % 54 !=0:
    latas = int(metros / 54) + 1
else:
    latas = metros / 54
valor = latas * 80

def main():
    print("%d lata(s) a um custo de %2f" %(latas,valor))
    print("latas %d" % latas)
    print("custo %2f" % valor)
if __name__ == '__main__':
    main()
