# -*- coding: utf-8 -*-
import math

def distancia(linha1,linha2):
    return ()
def main():
    linha1 = input().split(" ")
    linha2 = input().split(" ")

    x1,y1 = linha1
    x2,y2 = linha2

    distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
    print("%0.4f" % distancia)
if __name__ == '__main__':
    main()