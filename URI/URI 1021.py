# -*- coding: utf-8 -*-

def main():

    X = float(input())
    print("NOTAS:")

    for I in [100, 50, 20, 10, 5, 2]:
        J = int(X / I)
        print("%i nota(s) de R$ %i,00" % (J, I), end='\n')
        X = X - J * I

    print("MOEDAS:")

    for B in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
        C = int(X / B)
        print("%i moedas de R$ %1.2f" % (C, B), end='\n')
        X = X - C * B


if __name__ == '__main__':
    main()