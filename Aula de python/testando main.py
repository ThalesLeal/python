# -*- coding: utf-8 -*-

def media (A,B,C):
    return (A * 0.2)+(B * 0.3)+(C * 0.5)

def main():
    A = float(input(""))
    B = float(input(""))
    C = float(input(""))
    print("MEDIA = %2.1f" % media(A,B,C))
if __name__ == '__main__':
  main()