from Minimax import Minimax
from Interface import Interface
from Board import Board

class Game():
    def __init__(self):
        self.minimax = Minimax()
        self.interface = Interface()
        self.board = self.minimax.board
        self.PLAYER1 = +1
        self.PLAYER2 = -1

    def turns(self, players, player1_choice, player2_choice, depth):
        while depth > 0 and not self.board.game_over(self.PLAYER1, self.PLAYER2):
            if players == 0:
                depth = self.minimax.ai_turn(player1_choice, player2_choice, self.PLAYER1, self.PLAYER1, self.PLAYER2)
                depth = self.minimax.ai_turn(player1_choice, player2_choice, self.PLAYER2, self.PLAYER1, self.PLAYER2)
            elif players == 1:
                depth = self.minimax.human_turn(player1_choice, player2_choice, self.PLAYER1, self.PLAYER1, self.PLAYER2)
                depth = self.minimax.ai_turn(player1_choice, player2_choice, self.PLAYER2, self.PLAYER1, self.PLAYER2)
            elif players == 2:
                depth = self.minimax.human_turn(player1_choice, player2_choice, self.PLAYER1, self.PLAYER1, self.PLAYER2)
                depth = self.minimax.human_turn(player1_choice, player2_choice, self.PLAYER2, self.PLAYER1, self.PLAYER2)

    def startGame(self):
        players, player1_choice, player2_choice = self.interface.getInputs()
        self.turns(players, player1_choice, player2_choice, 9)
        self.board.endGame(player1_choice, self.PLAYER1, self.PLAYER2, player2_choice)
        exit()