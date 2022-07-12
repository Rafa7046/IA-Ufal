from Interface import Interface


class Board:

    def __init__(self):
        self.board = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]
        self.interface = Interface()

    def wins(self, state, player):
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def endGame(self, player1_choice, player1, player2, player2_choice):
        if self.wins(self.board, player1):
            self.interface.clean()
            print(f'Human turn [{player1_choice}]')
            self.render(self.board, player1_choice, player2_choice)
            print(f'{player1_choice} venceu!')
        elif self.wins(self.board, player2):
            self.interface.clean()
            print(f'Computer turn [{player2_choice}]')
            self.render(self.board, player1_choice, player2_choice)
            print(f'{player2_choice} venceu!')
        else:
            self.interface.clean()
            self.render(self.board, player1_choice, player2_choice)
            print('Empate!')

    def game_over(self, player1, player2):
        return self.wins(self.board, player2) or self.wins(self.board, player1)


    def empty_cells(self):
        cells = []

        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells


    def valid_move(self, x, y):
        if [x, y] in self.empty_cells():
            return True
        else:
            return False

    def render(self, state, player1_choice, player2_choice):
        chars = {
            -1: player2_choice,
            +1: player1_choice,
            0: ' '
        }
        str_line = '---------------'

        print('\n' + str_line)
        for row in state:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def set_move(self, x, y, player):
        if self.valid_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False