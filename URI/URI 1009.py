# -*- coding: utf-8 -*-

def vendedor(nome,salario_fixo, qtdvendas, bonus,total):
  return ()


def main():
    nome = input()
    salario_fixo = float(input())
    qtdvendas = float(input())

    bonus = float(qtdvendas * (15/100))

    total = salario_fixo + bonus

    print("TOTAL = R$ %5.2f" % total)
if __name__ == '__main__':
    main()