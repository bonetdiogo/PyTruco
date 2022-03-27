# PyTruco
O famoso jogo de cartas Truco, em Python. ("SEEEIS")

# Como jogar
Primeiro os jogadores recebem 3 cartas cada um e então comecam as rodadas
cada rodada os jogadores escolhem 1 de 3 ações: jogar, esconder e trucar.
IMPORTANTE: Rodadas são decididas no "melhor de 3".
            Vence quem possuir as cartas mais fortes ou se o outro jogador correr

Jogar: o jogador joga uma de suas cartas
Esconder: o jogador esconde uma de suas cartas no monte
Trucar: o jogador pede truco

Quando algum jogador tiver trucado a rodada vale 3 tentos (pontos)
O outro jogador pode escolher entre correr, aceitar ou aumentar

Correr: o jogador que pediu truco ganha 1 ponto
Aceitar: o jogador que ganhar a rodada leva os 3 pontos
Aumentar: o jogador pode pedir por 6 pontos e o outro pode pedir por 9 e então 12
          no case de um jogador correr após pedirem 6 o outro recebe 3 tentos,
          se for valendo 9 o outro recebe 6 e assim por diante.
          
O jogo inteiro vai até 12 tentos, sendo o matchpoint um pouco diferente...
Se um dos jogadores possuir 11 tentos, o jogo automaticamente está trucado
Em casos de partidas 2x2, a dupla pode analisar as cartas um do outro e
decidir se vão jogar a rodada.
