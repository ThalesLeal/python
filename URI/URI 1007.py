# -*- coding: utf-8 -*-

def DIFERENCA (A,B,C,D):
    return (A * B - C * D)

def main():
    A = int(input(""))
    B = int(input(""))
    C = int(input(""))
    D = int(input(""))

    print("DIFERENCA = %i" % DIFERENCA(A,B,C,D))
if __name__ == '__main__':
  main()