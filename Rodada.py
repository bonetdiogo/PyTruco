import random

class Rodada():
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.manilha = 0

    def JogarJogo(self):
        continuarJogo = True

        while continuarJogo:
            self.MostrarPlacar()
            self.JogarRodada()
            continuarJogo = self.jogadores[0].tentos < 12 and self.jogadores[1].tentos < 12

        # Confere qual dos jogadores venceu o jogo
        for jogador in self.jogadores:
            if (jogador.tentos >= 12):
                vencedorJogo = jogador

        print(vencedorJogo, 'VENCEU O JOGO TRUCO!!!')

    def MostrarPlacar(self):
        jogador1 = self.jogadores[0]
        jogador2 = self.jogadores[1]

        print()
        print('O jogo está:', jogador1.nome, jogador1.tentos, 'X', jogador2.tentos, jogador2.nome)
        print()

    def JogarRodada(self):
        continuarRodada = True

        while continuarRodada:
            for jogador in self.jogadores:
                print('É a vez de', jogador.nome)
                self.EscolheAcao(jogador)

            vencedor = self.QuemVence()

            vencedor.pontosRodada += 1
            self.AnunciaVencedor(vencedor)
            self.RemoverCartasUsadas()

            # Continua rodada se nenhum dos jogadores possui 2 pontos
            continuarRodada = self.jogadores[0].pontosRodada < 2 and self.jogadores[1].pontosRodada < 2

        # Confere qual dos jogadores venceu a rodada
        for jogador in self.jogadores:
            if (jogador.pontosRodada >= 2):
                vencedorRodada = jogador
            jogador.pontosRodada = 0

        print('=============')
        print('Fim Da Rodada', vencedorRodada.nome, 'Venceu')
        print('=============')

    def EscolheAcao(self, jogador):
        acao = input('Escolha a ação (jogar/esconder/trucar): ')

        if (acao == 'jogar'):
            jogador.PrintOpcoesCartas()
            self.EscolherCarta(jogador, acao)
        elif (acao == 'esconder'):
            jogador.PrintOpcoesCartas()
            self.EscolherCarta(jogador, acao)
        elif (acao == 'trucar'):
            self.JogoTrucado
            print('TRUUUUCO (ainda não funciona)')
        else:
            print('Comando inválido, tente novamente')
            print()
            self.EscolheAcao(jogador)

    def AnunciaVencedor(self, vencedor):
        print(vencedor.nome, 'vence o jogo com', vencedor.cartaAtual.NomeInteiro())

    def RemoverCartasUsadas(self):
        for jogador in self.jogadores:
            jogador.cartas.remove(jogador.cartaAtual)

    def EscolherCarta(self, jogador, acao):
        frase = 'Qual carta vai ' + acao + '? '
        opcao = int(input(frase))
        cartaInvalida = True

        for carta in jogador.cartas:
            if (carta.id == opcao):
                cartaInvalida = False
                jogador.cartaAtual = carta
                print(jogador.nome, 'jogou um', carta.NomeInteiro())

        if (cartaInvalida == True):
            print()
            print('Carta inválida, tente novamente.')
            print()
            self.EscolherCarta(jogador, acao)

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

        carta1 = self.jogadores[0].cartaAtual
        carta2 = self.jogadores[1].cartaAtual

        # Os 2 jogadores possuem manilha, decide no naipe
        if (carta1.valor  == carta2.valor == self.manilha.valor):
            if (carta1.naipe > carta2.naipe):
                return self.jogadores[0]
            else:
                return self.jogadores[1]

        # Empatou e nenhum possui manilha
        elif (carta1.valor == carta2.valor != self.manilha.valor):
            return 0

        # Cartas diferentes, ganha a maior, mas perde se a outra for manilha
        elif (carta1.valor > carta2.valor):
            if (carta2 != self.manilha.valor):
                return self.jogadores[0]
            else:
                return self.jogadores[1]
        elif (carta1.valor < carta2.valor):
            if (carta1.valor != self.manilha.valor):
                return self.jogadores[1]
            else:
                return self.jogadores[0]