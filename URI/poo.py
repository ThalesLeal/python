##criando as classe e seus construtores##
class Veiculo:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def liga(self):
        print("Veiculo ligado")


class Carro(Veiculo):
    def __init__(self, nome, marca):
        super().__init__(nome, marca)
