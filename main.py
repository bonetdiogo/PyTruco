import Rodada
import Carta
import Jogador

def CriarCartas():
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    naipes = [1, 2, 3, 4]
    listaCartas = []

    # Cria todas as cartas possíveis (40) e adiciona a lista
    for valor in valores:
        for naipe in naipes:
            carta = Carta.Carta(valor, naipe)
            listaCartas.append(carta)
    return listaCartas

def CriarJogadores():
    nomeJogador1 = input('Insira nome do jogador 1: ')
    nomeJogador2 = input('Insira nome do jogador 2: ')

    jogador1 = Jogador.Jogador(nomeJogador1, 0)
    jogador2 = Jogador.Jogador(nomeJogador2, 0)
    return [jogador1, jogador2]

cartas = CriarCartas()
jogadores = CriarJogadores()
rodadaAtual = Rodada.Rodada(jogadores)
rodadaAtual.DistribuirCartas(cartas)

# Ações dos jogadores
rodadaAtual.JogarJogo()




