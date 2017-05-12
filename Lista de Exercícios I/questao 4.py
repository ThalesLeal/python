##4) Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.


def main():
    salario =(input("Digite seu salario"))
    aumento =(input("quantos %"))

    novo_salario = str(salario /100.0 * aumento)

    print % str(aumento)+"%de"+ str(salario)+"foi"+novo_salario

if __name__ == '__main__':
    main()
