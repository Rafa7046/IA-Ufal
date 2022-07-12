import platform
from os import system

class Interface:

    def clean(self):
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    def getInputs(self):
        self.clean()
        players = int(input("Quais serão os jogadores\n[0]: Duas Ias\n[1]: Uma Ia e um jogador\n[2]: Dois joagadores\n"))
        player2_choice = ''
        player1_choice = ''

        if players == 0:
            player2_choice = 'X'  # X or O
            player1_choice = 'O'
        else:
            while player1_choice != 'O' and player1_choice != 'X':
                try:
                    print('')
                    player1_choice = input('Escolha X or O\Escolhido: ').upper()
                except (EOFError, KeyboardInterrupt):
                    print('Bye')
                    exit()
                except (KeyError, ValueError):
                    print('Bad choice')
            if player1_choice == 'X':
                player2_choice = 'O'
            else:
                player2_choice = 'X'
        self.clean()

        return players, player1_choice, player2_choice