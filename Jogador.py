class Jogador():
    def __init__(self, nome, tentos):
        self.nome = nome
        self.tentos = tentos
        self.pontosRodada = 0
        self.cartaAtual = 0
        self.cartas = []

    def PrintOpcoesCartas(self):
        print()
        print(self.nome, 'possui as cartas:')
        for carta in self.cartas:
            print(carta.id, '-', carta.NomeInteiro())