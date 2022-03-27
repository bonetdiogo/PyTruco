import random

class Rodada():
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.manilha = 0

    def JogarRodada(self):

        for jogador in self.jogadores:
            print('É a vez de', jogador.nome)
            acao = input('Escolha a ação (jogar/esconder/trucar): ')

            if (acao == 'jogar'):
                self.EscolherCartaAtual(jogador, acao)
            elif (acao == 'esconder'):
                self.EscolherCartaAtual(jogador, acao)
            elif (acao == 'trucar'):
                print('TRUUUUCO (ainda não funciona)')

        vencedorRodada = self.QuemVence()


    def EscolherCartaAtual(self, jogador, acao):
        jogador.PrintOpcoesCartas()

        frase = 'Qual carta vai ' + acao + '? '
        opcao = int(input(frase))

        for carta in jogador.cartas:
            if (carta.id == opcao):
                jogador.cartaAtual = carta
                print(jogador.nome, 'jogou um', carta.NomeInteiro())
                print()

    # Passa por todos os jogadores, escolhe uma carta aleatória,
    # entrega ao jogador e a remove da lista, depois seleciona o vira
    def DistribuirCartas(self, cartas):
        maxCartas = 3
        id = 1

        for jogador in self.jogadores:
            print('\n', jogador.nome, ' recebeu as cartas:', sep='')
            while id < maxCartas + 1:
                cartaEscolhida = random.choice(cartas)
                jogador.cartas.append(cartaEscolhida)
                cartas.remove(cartaEscolhida)
                cartaEscolhida.DefinirId(id)
                print(cartaEscolhida.NomeInteiro())
                id += 1

            id = 1

        self.manilha = random.choice(cartas)
        print('\n', 'Manilha são as cartas: ', self.manilha.NomeValor(), '\n',  sep='')

    # Ainda vou simplificar o código
    def QuemVence(self):

        carta1 = self.jogadores[0]
        carta2 = self.jogadores[1]

        # Os 2 jogadores possuem manilha, decide no naipe
        if (carta1.valor  == carta2.valor == self.manilha.valor):
            if (carta1.naipe > carta2.naipe):
                return jogador1
            else:
                return jogador2

        # Empatou e nenhum possui manilha
        elif (carta1.valor == carta2.valor != self.manilha.valor):
            return 0

        # Cartas diferentes, ganha a maior, mas perde se a outra for manilha
        elif (carta1.valor > carta2.valor):
            if (carta2 != self.manilha.valor):
                return jogador1
            else:
                return jogador2
        elif (carta1.valor < carta2.valor):
            if (carta1.valor != self.manilha.valor):
                return jogador2
            else:
                return jogador1