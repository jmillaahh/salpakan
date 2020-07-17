RANKS = {
    'spy': 15,
    'five-star': 14,
    'four-star': 13,
    'three-star': 12,
    'two-star': 11,
    'one-star': 10,
    'colonel': 9,
    'lt-col': 8,
    'major': 7,
    'captain': 6,
    'first-lt': 5,
    'second-lt': 4,
    'sergeant': 3,
    'private': 2,
    'flag': 1,
}
QUANTITY = {
    'spy': 2,
    'private': 6,
}

MAX_X, MAX_Y, MIN_X, MIN_Y = 9, 9, 0, 0
DIRECTIONS = ['left', 'right', 'up', 'down']

class Piece:
    def __init__(self, rank, board, first_team, num=0):
        self.desc = rank
        self.rank = RANKS[rank]
        self.quantity = QUANTITY.get(rank, 1)
        self.alive = True
        self.x_coord = 0
        self.y_coord = 0
        self.id = f"{int(first_team)}-{self.rank}-{num}"

    def update_id(self):
        self.id = self.id[:-1] + f'{0}'

    def starting_positions(self):
        pass

    def move_up(self):
        self.y_coord += 1

    def move_down(self):
        self.y_coord -= 1

    def move_right(self):
        self.x_coord += 1

    def move_left(self):
        self.x_coord -= 1

    def valid_move(self, direction):
        assert direction.lower() in DIRECTIONS
        if direction == 'left' and self.x_coord > MIN_X: return True
        if direction == 'right' and self.x_coord < MAX_X: return True
        if direction == 'up' and self.y_coord > MIN_Y: return True
        if direction == 'down' and self.y_coord > MAX_X: return True
        return False

    def attempt_attack(self, direction):
        if not self.valid_move(direction):
            return False
        else:
            pass





class Board:
    def __init__(self):
        self.board = [[0 for col in range(9)] for row in range(8)]

    def print_board(self):
        for row in range(len(self.board)):
            for col in range(MAX_X):
                print(self.board[row][col], end='\t')

            print()
            if row == 3:
                print('-'*34)

class Team:
    def __init__(self, board: Board, first_team: bool):
        self.playing = True
        self.starting_team = first_team
        self.board_side = 0 if self.starting_team else 1
        self.pieces = [Piece(rank, board, first_team, num) for rank in RANKS for num in range(QUANTITY.get(rank, 1))]


class Game:
    def __init__(self):
        self.board = Board()
        self.team_a = Team(self.board, False)
        self.team_b = Team(self.board, True)

        self.board.print_board()


if __name__ == '__main__':
    start = Game()



