## de 400 ano 365 mes 30 saida 1 ano 1 mes 5 dias
def idade_dias(dia,ano):
    return()

def main():
    dias = int(input())
    ano = int(dias / 365)
    aux = dias % 365

    meses = int(aux / 30)
    dias = aux % 30

    print("%i anos(s)" % ano,end='\n')
    print("%i mes(es)" % meses,end='\n')
    print("%i dia(s)" %dias,end='\n')
if __name__ == '__main__':
    main()