minutos = int(input("Digite quantos minutos vc usou"))
if   minutos < 200:
     preço = 0.20

elif minutos <=400:
     preço = 0.18

elif minutos <=800:
     preço = 0.15
else:
    preço = 0.08

print("Conta de telefone foi :  R$%6.2f" % (minutos * preço))