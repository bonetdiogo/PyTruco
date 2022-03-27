class Carta():
    def __init__(self, valor, naipe):
        self.id = 0
        self.valor = valor
        self.naipe = naipe

    def DefinirId(self, id):
        self.id = id

    def NomeInteiro(self):

        if (self.valor == 10): numero = '3'
        if (self.valor == 9):  numero = '2'
        if (self.valor == 8):  numero = 'A'
        if (self.valor == 7):  numero = 'K'
        if (self.valor == 6):  numero = 'J'
        if (self.valor == 5):  numero = 'Q'
        if (self.valor == 4):  numero = '7'
        if (self.valor == 3):  numero = '6'
        if (self.valor == 2):  numero = '5'
        if (self.valor == 1):  numero = '4'

        if (self.naipe == 4): naipe = '♣ Paus'
        if (self.naipe == 3): naipe = '♥ Copa'
        if (self.naipe == 2): naipe = '♠ Espada'
        if (self.naipe == 1): naipe = '♦ Ouros'

        return numero + ' de ' + naipe

    def NomeValor(self):
        if (self.valor == 10): return '3'
        if (self.valor == 9):  return '2'
        if (self.valor == 8):  return 'A'
        if (self.valor == 7):  return 'K'
        if (self.valor == 6):  return 'J'
        if (self.valor == 5):  return 'Q'
        if (self.valor == 4):  return '7'
        if (self.valor == 3):  return '6'
        if (self.valor == 2):  return '5'
        if (self.valor == 1):  return '4'