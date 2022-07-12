from Board import Board
from Interface import Interface
from math import inf
from random import choice
import time

class Minimax:

    def __init__(self):
        self.board = Board()
        self.interface = Interface()

    def evaluate(self, state, player1, player2):
        if self.board.wins(state, player1):
            score = +1
        elif self.board.wins(state, player2):
            score = -1
        else:
            score = 0

        return score

    def minimax(self, state, depth, player, player1, player2):
        if player == player1:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if depth == 0 or self.board.game_over(player1, player2):
            score = self.evaluate(state, player1, player2)
            return [-1, -1, score]

        for cell in self.board.empty_cells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player, player1, player2)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == player1:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def ai_turn(self, player1_choice, player2_choice, player, player1, player2):
        depth = len(self.board.empty_cells())
        if depth == 0 or self.board.game_over(player1, player2):
            return depth

        if player == player1:
            playerchoice = player1_choice
        else:
            playerchoice = player2_choice
        self.interface.clean()
        print(f'Vez do computador [{playerchoice}]')
        self.board.render(self.board.board, player1_choice, player2_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(self.board.board, depth, player, player1, player2)
            x, y = move[0], move[1]

        self.board.set_move(x, y, player)
        time.sleep(1)

        return depth

    def human_turn(self, player1_choice, player2_choice, player, player1, player2):
        depth = len(self.board.empty_cells())
        if depth == 0 or self.board.game_over(player1, player2):
            return depth

        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        if player == player1:
            playerchoice = player1_choice
        else:
            playerchoice = player2_choice
        self.interface.clean()
        print(f'Vez do Jogador [{playerchoice}]')
        self.board.render(self.board.board, player1_choice, player2_choice)

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = self.board.set_move(coord[0], coord[1], player)

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        return depth
