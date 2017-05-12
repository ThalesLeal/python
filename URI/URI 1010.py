# -*- coding: utf-8 -*-

def calculo_simples(linha1,linha2,total):
    return ()

def main():
    linha1 = input().split(" ")
    linha2 = input().split(" ")

    cod1, qtde1, valor1 = linha1
    cod2, qtde2, valor2 = linha2

    total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

    print("VALOR A PAGAR: R$ %0.2f" % total)
if __name__ == '__main__':
    main()