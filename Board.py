import pygame
from Shape import Shape


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

    def change_field(self):
        self.board = [[0] * self.width for _ in range(self.height)]