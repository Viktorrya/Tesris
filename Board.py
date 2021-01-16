import pygame
from Shape import Shape


class Board:
    # создание поля
    def __init__(self):
        self.width = 500
        self.height = 800
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
                    pygame.draw.rect(screen, (self.board[i][j][0] // 2, self.board[i][j][1] // 2,
                                              self.board[i][j][2] // 2),
                                     (self.cell_size * j,
                                      self.cell_size * i,
                                      self.cell_size, self.cell_size))

    def change_field(self):
        self.board = [[0] * self.width for _ in range(self.height)]