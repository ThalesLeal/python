# -*- coding: utf-8 -*-


def calcula_salario(qtdhoras, valorHoras):
    return (qtdhoras * valorHoras)

def main():
    numero = int(input())
    qtdhoras = int(input())
    valorHoras = float(input())

    print("NUMBER = %i" % numero)
    print("SALARY = U$ %5.2f" % calcula_salario(qtdhoras,valorHoras))

if __name__ == '__main__':
    main()