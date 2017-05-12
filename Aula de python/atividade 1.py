velocidade =int(input("Digite sua velocidade"))

if    velocidade<=110:
      print("velocidade permitida")


elif velocidade > 110:
     print("vc levou uma multado")
     multa= (velocidade-110)*5
     print("Valor da multa %5.2f" %multa)