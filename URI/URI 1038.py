def menu():
    escolha = int(input('''
    Codigo Especificação Preço
    1 -Cachorro Quente R$ 4.00
    2 -    X-Salada    R$ 4.50
    3 -    X-Bacon     R$ 5.00
    4 -Torrada simples R$ 2.00
    5 -   Refrigerante R$ 1.50
    0 - SAIR
    
    ESCOLHA:'''))
    if escolha == 1:
        print("Opção 1 escolhida")
    elif escolha == 2:
        print("Opção 2 escolhida")
    elif escolha == 3:
        print("Opção 3 escolhida")
    elif escolha == 4:
        print("Opção 4 escolhida")
    elif escolha == 5:
        print("Opção 5 escolhida")
    elif escolha == 0:
        print("Saiu")
menu()
