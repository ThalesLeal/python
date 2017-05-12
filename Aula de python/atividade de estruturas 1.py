minutos =int(input("Digite quantos minutos vc usou"))

if minutos <=200:
    preço = 0.20
else:
    if minutos <=400:
       preço = 0.18
    else:
        if minutos <=800:
            preço = 0.15
        else:
            preço = 0.08

print("Sua conta de telefone foi: %6.2f" % (minutos * preço))