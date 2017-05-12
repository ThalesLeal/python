## de 400 ano 365 mes 30 saida 1 ano 1 mes 5 dias
def idade_dias(dia,ano):
    return()

def main():
    dia = int(input())
    ano = int(dia / 365)
    aux = dia % 365

    mes = int(aux / 30)
    dia = aux % 30

    print("%i ano(s)"% ano,end='\n')
    print("%i mes(es)"% mes,end='\n')
    print("%i dia(s)"%dia,end='\n')
if __name__ == '__main__':
    main()
