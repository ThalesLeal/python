# -*- coding: utf-8 -*-

def consumo(x,y,consumo_por_litro):
    return ()


def main():
    x = float(input())
    y = float(input())

    consumo_por_litro = x / y
    print("%5.3f" % consumo_por_litro,"km/l")

if __name__ == '__main__':
    main()