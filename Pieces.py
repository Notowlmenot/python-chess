WHITE = "white"
BLACK = "black"


class Piece:
    def __init__(self, color, y, x):
        self.x = x
        self.y = y
        self.color = color
        self.name = ''

    def __str__(self):
        return self.name


class Pawn(Piece):
    is_first = True

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if self.color == WHITE:
            self.name = 'P'

        else:
            self.name = 'p'

    def move(self, x, y, gameboard):
        if self.color == WHITE:
            kf = -1

        else:
            kf = 1

        if (self.is_first == True and (self.y - y) * kf == 2 and self.x - x == 0) or ((self.y - y) * kf == 1 and self.x - x == 0) or ((self.y - y) * kf == 1 and abs(self.x - x) == 1 and gameboard[(y, x)] != ' ' and gameboard[(y, x)].color != self.color):
            if (abs(self.y - y) == 1) and (abs(self.x - x) != 1) and (gameboard[(y, x)] != ' ') and (
                    gameboard[(y, x)].color != self.color):
                return
            else:
                gameboard[(y, x)] = gameboard[(self.y, self.x)]
                gameboard[(self.y, self.x)] = ' '
                print(abs(self.y - y))
                self.x, self.y = x, y
                self.is_first = False
                return True


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if self.color == WHITE:
            self.name = 'N'
        else:
            self.name = 'n'

    def move(self, x, y, gameboard):
        if (abs(x - self.x) == 2 and abs(y - self.y) == 1) or (abs(x - self.x) == 1 and abs(y - self.y) == 2):
            if (gameboard[(y, x)] == ' ') or (gameboard[(y, x)].color != self.color):
                gameboard[(y, x)] = gameboard[(self.y, self.x)]
                gameboard[(self.y, self.x)] = ' '
                self.x, self.y = x, y
                return True
            else:
                return False


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if self.color == WHITE:
            self.name = 'R'
        else:
            self.name = 'r'

    def move(self, x, y, gameboard):
        is_Trueturn = False
        is_break = False
        if self.x - x == 0:
            direction = (self.y - y) // abs(self.y - y)
            for i in range(direction, (self.y - y), direction):
                if gameboard[(self.y - i, self.x)] == ' ':
                    is_Trueturn = True
                else:
                    is_Trueturn = False
                    is_break = True
                    break
            if not is_break and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
                is_Trueturn = True
            else:
                is_Trueturn = False

        elif self.y == y:
            direction = (self.x - x) // abs(self.x - x)
            for i in range(direction, (self.x - x), direction):
                if gameboard[(self.y, self.x - i)] == ' ':
                    is_Trueturn = True
                else:
                    is_Trueturn = False
                    is_break = True
                    break
            if not is_break and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
                is_Trueturn = True
            else:
                is_Trueturn = False

        if is_Trueturn == True:
            gameboard[(y, x)] = gameboard[(self.y, self.x)]
            gameboard[(self.y, self.x)] = ' '
            self.x, self.y = x, y
            return True


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if self.color == WHITE:
            self.name = 'B'
        else:
            self.name = 'b'

    def move(self, x, y, gameboard):
        is_Trueturn = False
        is_break = False
        if abs(self.x - x) == abs(self.y - y):
            x_dir, y_dir = (x - self.x) // abs(self.x - x), (y - self.y) // abs(self.y - y)
            for i in range(1, abs(self.x - x)):
                if gameboard[(self.x + i * x_dir, self.y + i * y_dir)] == ' ':
                    is_Trueturn = True
                else:
                    is_Trueturn = False
                    is_break = True
                    break
            if not is_break and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
                is_Trueturn = True
            else:
                is_Trueturn = False
            if is_Trueturn:
                gameboard[(y, x)] = gameboard[(self.y, self.x)]
                gameboard[(self.y, self.x)] = ' '
                self.x, self.y = x, y
                return True


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if self.color == WHITE:
            self.name = 'Q'
        else:
            self.name = 'q'

    def move(self, x, y, gameboard):
        is_break = False
        is_Trueturn = True
        if self.x - x == 0:
            direction = (self.y - y) // abs(self.y - y)
            for i in range(direction, (self.y - y), direction):
                if gameboard[(self.y - i, self.x)] == ' ':
                    is_Trueturn = True
                else:
                    is_Trueturn = False
                    is_break = True
                    break
            if not is_break and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
                is_Trueturn = True
            else:
                is_Trueturn = False

        elif self.y - y == 0:
            direction = (self.x - x) // abs(self.x - x)
            for i in range(direction, (self.x - x), direction):
                if gameboard[(self.y, self.x - i)] == ' ':
                    is_Trueturn = True
                else:
                    is_Trueturn = False
                    is_break = True
                    break
            if not is_break and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
                is_Trueturn = True
            else:
                is_Trueturn = False

        elif abs(self.x - x) == abs(self.y - y):
            x_dir, y_dir = (x - self.x) // abs(self.x - x), (y - self.y) // abs(self.y - y)
            for i in range(1, abs(self.x - x)):
                if gameboard[(self.y + i * y_dir, self.x + i * x_dir)] == ' ':
                    is_Trueturn = True
                else:
                    is_Trueturn = False
                    is_break = True
                    break
            if not is_break and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
                is_Trueturn = True
            else:
                is_Trueturn = False

        if is_Trueturn:
            gameboard[(y, x)] = gameboard[(self.y, self.x)]
            gameboard[(self.y, self.x)] = ' '
            self.x, self.y = x, y
            return True


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if self.color == WHITE:
            self.name = 'K'
        else:
            self.name = 'k'

    def move(self, x, y, gameboard):
        if abs(self.x - x) < 2 and (abs(self.y - y) < 2) and (gameboard[(y, x)] == ' ' or gameboard[(y, x)].color != self.color):
            gameboard[(y, x)] = gameboard[(self.y, self.x)]
            gameboard[(self.y, self.x)] = ' '
            self.x, self.y = x, y
            return True
