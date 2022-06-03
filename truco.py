from random import choice
from time import time


class Truco:
    def __init__(self):
        
        #placar
        self.pontos_time1 = 0
        self.pontos_time2 = 0

        #jogadores
        self.player1, self.player2, self.player3, self.player4 = [], [], [], []

        #funções do jogo
        self.maquina = 0
        self.manilha = 0
        self.rodada = 0

        #dicionário com as cartas e seus pesos
        self.cartas = {
            3: {
                "paus": 10,
                "copas": 10,
                "espadas": 10,
                "moles": 10
            },
            2: {
                "paus": 9,
                "copas": 9,
                "espadas": 9,
                "moles": 9
            },
            1: {
                "paus": 8,
                "copas": 8,
                "espadas": 8,
                "moles": 8
            },
            12: {
                "paus": 7,
                "copas": 7,
                "espadas": 7,
                "moles": 7
            },
            11: {
                "paus": 6,
                "copas": 6,
                "espadas": 6,
                "moles": 6
            },
            10: {
                "paus": 5,
                "copas": 5,
                "espadas": 5,
                "moles": 5
            },
            7: {
                "paus": 4,
                "copas": 4,
                "espadas": 4,
                "moles": 4
            }, 
            6: {
                "paus": 3,
                "copas": 3,
                "espadas": 3,
                "moles": 3
            }, 
            5: {
                "paus": 2,
                "copas": 2,
                "espadas": 2,
                "moles": 2
            }, 
            4: {
                "paus": 1,
                "copas": 1,
                "espadas": 1,
                "moles": 1
            }
        }

        #criar o peso das maquinas para definir a manilha
        self.manilhas = {
            3: 4,
            2: 3,
            1: 2,
            12: 1,
            11: 12,
            10: 11,
            7: 10,
            6: 7,
            5: 6,
            4: 5,
        }

    def definir_manilha(self):
        # definindo a maquina e a manilha
        self.maquina = choice([*self.cartas.keys()])
        self.manilha = self.manilhas[self.maquina]
        print("="*60)
        print(f"a maquina é o {self.maquina}, a manilha é o {self.manilha}")

        #atualizando o peso da manilha
        self.cartas.update({self.manilha: {"paus": 14, "copas": 13, "espadas": 12, "moles": 11}})
        '''for i in self.cartas:
            print(self.cartas[i])'''

    def distribuir_cartas(self):
        #definir a manilha
        self.definir_manilha()

        # criando as cartas
        cartas = []
        for i in self.cartas.keys():
            for j in self.cartas[i]:
                cartas.append([i, j])

        def remover(i):
            cartas.remove(i)
            return i

        # distribuindo as cartas
        self.player1 = ["jogador 1", *[remover(choice(cartas)) for _ in range(1, 4)]]
        self.player2 = ["jogador 2", *[remover(choice(cartas)) for _ in range(1, 4)]]
        self.player3 = ["jogador 3", *[remover(choice(cartas)) for _ in range(1, 4)]]
        self.player4 = ["jogador 4", *[remover(choice(cartas)) for _ in range(1, 4)]]

        self.rodadas() #iniciar as rodadas

    def rodadas(self):
        if self.rodada % 4 == 0: #pra definir quem começa no bgl
            jogadores = [self.player1, self.player2, self.player3, self.player4] #definir a ordem dos jogadores
            self.jogar(jogadores) #iniciar o jogo    
        elif self.rodada % 4 == 1:
            jogadores = [self.player2, self.player3, self.player4, self.player1] #definir a ordem dos jogadores
            self.jogar(jogadores)
        elif self.rodada % 4 == 2:
            jogadores = [self.player3, self.player4, self.player1, self.player2] #definir a ordem dos jogadores
            self.jogar(jogadores)
        elif self.rodada % 4 == 3:
            jogadores = [self.player4, self.player1, self.player2, self.player3] #definir a ordem dos jogadores
            self.jogar(jogadores)

        self.rodada += 1

    def jogar(self, jogadores: list):
        t1, t2 = 0, 0 #definir os pontos dos times
        string_random = "(1, 2, 3)" #string para aparecer no bgl de pedir a carta
        for _ in range(1, 4): #numero de rounds da rodada
            maior = 0 #definir a carta mais forte
            print("="*60) #print random
            '''print(*self.player1)
            print(*self.player2)
            print(*self.player3)
            print(*self.player4)'''#mostrar as cartas de todos
            print("RODADA: "+str(_)) #sinalizar a rodada

            for player in jogadores:
                print("="*60)
                print(f"é a vez do {player[0]}")
                print(f"suas cartas: {player[1:]}")

                carta = player[int(input(f"Qual carta deseja jogar? {string_random}: "))]

                print(f"carta jogada: {carta}")

                if self.cartas[carta[0]][carta[1]] > maior:
                    maior = self.cartas[carta[0]][carta[1]]
                    pontuador = player
                    print(f"o pontuador atual é o {pontuador} com uma carta de peso {maior}")
                elif self.cartas[carta[0]][carta[1]] == maior:
                    if int(player[0][-1]) % 2 == 0 and int(pontuador[0][-1]) % 2 == 0 or int(player[0][-1]) % 2 != 0 and int(pontuador[0][-1]) % 2 != 0:
                        maior = self.cartas[carta[0]][carta[1]]
                        pontuador = player
                    else:
                        maior = self.cartas[carta[0]][carta[1]]
                        pontuador = ["ninguém"]

                player.remove(carta)
            
            print(f"{pontuador[0]} venceu esta rodada")
            string_random = string_random[:-4]+")"
            if pontuador[0] != "ninguém":
                jogadores = jogadores[jogadores.index(pontuador):]+ jogadores[:jogadores.index(pontuador)]
         

truco = Truco()
while True:
    truco.distribuir_cartas()
