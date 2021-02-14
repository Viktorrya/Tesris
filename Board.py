import pygame


class Board:
    # создание поля
    def __init__(self):
        self.width = 10
        self.height = 16
        self.board = [[(0, 0, 0)] * self.width for _ in range(self.height)]
        self.cell_size = 50

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == (0, 0, 0):
                    pygame.draw.rect(screen, (50, 50, 50),
                                     (self.cell_size * j,
                                      self.cell_size * i,
                                      self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, self.board[i][j],
                                 (self.cell_size * j,
                                  self.cell_size * i,
                                  self.cell_size, self.cell_size))

    def check_line(self):
        count = 0
        for i in range(len(self.board)):
            print(self.board[i])
            for j in self.board[i]:
                if j != (0, 0, 0):
                    count += 1
            if count == len(self.board[i]):
                self.board[i] = [(0, 0, 0)] * self.width
                for _ in range(len(self.board) - 2, -1, -1):
                    if _ <= i:
                        self.board[_] = self.board[_ + 1]

    def check_defeat(self):
        if self.board[0] != [(0, 0, 0)] * self.width:
            return True
        return False


