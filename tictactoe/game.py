from player import HumanPlayer, RandomComputerPlayer, UnbeatableAIPlayer
import time

class TicTacToe:
    def __init__(self): # we need a board
        self.board = [' ' for _ in range(9)] # we will use a single list to represent a 3x3 board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] # this is a list comprehension (condenses the for loop into 1-liner)
        # moves = []
        # for (i, x) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         # available move
        #         moves.append(i)
        # return moves
    
    def empty_squares(self):
        #check if any empty squares on the board
        return ' ' in self.board
    
    # this will count the number of spaces:
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere: row / column / diagonal
        # check row:  
        row_ind = square // 3 # divide by 3 and round down
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column: divide by 3 and take left over -> so modulo
        col_ind = square % 3
        column = [self.board[col_ind + i*3]  for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these checks fail -> we dont have a winner
        return False

def play(game, x_player, o_player, print_game=True):
    # returns winnner of game (the letter); or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner bc we'll just return that which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)  
        
        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #empty line
            
            if game.current_winner:
                # if we have a winner -> game is finished
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches the player

        if print_game:
            time.sleep(0.8)

    if print_game:
        print('Its a tie!')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = RandomComputerPlayer('X')
        o_player = UnbeatableAIPlayer('O')
        t = TicTacToe() # our game
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    print(f'X wins: {x_wins} times.')
    print(f'O wins: {o_wins} times.')
    print(f'Ties: {ties} times.')


