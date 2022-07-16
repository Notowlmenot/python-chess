from Pieces import *
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def translator(current_figure):
    if len(current_figure) >= 2 and 'A' <= current_figure[0].upper() <= 'H' and '1' <= current_figure[1] <= '8':
        x = ord(current_figure[0].upper()) - ord('A')
        y = int(current_figure[1]) - 1
    else:
        cls()
        print('Некорректная фигура или ход')
        x, y = -1, -1
    return x, y


class Game:
    def __init__(self):
        self.colorturn = 1
        self.gameboard = {}
        self.playersturn = 'white'
        self.placeFigures()
        self.right_Turn = False

    def printBoard(self):
        print("  A | B | C | D | E | F | G | H |")
        for i in range(0, 8):
            print("-" * 32)
            print(i + 1, end="|")
            for j in range(0, 8):
                item = self.gameboard.get((i, j), " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 32)

    def placeFigures(self):
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(0, 8):
            self.gameboard[(1, i)] = Pawn(WHITE, 1, i)
            self.gameboard[(6, i)] = Pawn(BLACK, 6, i)
            self.gameboard[(0, i)] = figures[i](WHITE, 0, i)
        figures.reverse()
        for i in range(0,8):
            self.gameboard[(7, i)] = figures[i](BLACK, 7, i)
        for i in range(2, 6):
            for k in range(0, 8):
                self.gameboard[(i, k)] = ' '

    def chooseFigure(self):
        current_figure = input('Выберите фигуру: ')
        x, y = translator(current_figure)
        if x != -1:
            if self.gameboard[(y,x)] != ' ':
                    print(f'Выбранная фигура - {self.gameboard[(y, x)]}')
                    current_move = input('Выберите ход: ')
                    x1, y1 = translator(current_move)
                    if self.gameboard[(y, x)].name != ' ' and self.gameboard[(y, x)].color != self.playersturn:
                        cls()
                        print('Выбрана фигура неверного цвета. Текущий ход -', self.playersturn)
                        return
                    if self.gameboard[(y, x)].move(x1, y1, self.gameboard):
                        self.colorturn = self.colorturn * -1
                        cls()
                    else:
                        cls()
                        print('Некорректный ход. ')

    def main(self):
        while True:
            self.printBoard()
            if self.colorturn == 1:
                print('Ход белых.')
                self.playersturn = 'white'
            else:
                print('Ход черных.')
                self.playersturn = 'black'

            self.chooseFigure()


if __name__ == "__main__":
    Game().main()
