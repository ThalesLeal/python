##3) Escreva um programa que leia a quantidade de dias, horas,
# minutos e segundos do usuário. Calculeo total em segundos.

def main():
    dias = input("Digite uma quantidade de dias: ")
    horas = input("Digite uma quantidade de horas: ")
    minutos = input("Digite uma quantidade de minutos: ")
    segundos = input("Digite uma quantidade de segundos: ")

    totalSegundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

    print (dias, "dias", horas, "horas", minutos, "minutos", segundos)
    print("segundos representam", totalSegundos, "segundos")


if __name__ == '__main__':
    main()

