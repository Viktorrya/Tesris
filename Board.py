import pygame


class Board:
    # создание поля
    def __init__(self):
        self.width = 10
        self.height = 16  # всю таблицу будем заполнять цветами клеток
        self.board = [[(0, 0, 0)] * self.width for _ in range(self.height)]
        self.cell_size = 50

    def render(self, screen):  # отрисовка
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

    def check_line(self):  # проверка линий
        for i in range(len(self.board)):
            count = 0
            for j in self.board[i]:
                if j != (0, 0, 0):
                    count += 1
            if count == 10:  # если все клетки в данной строчке не чёрные,
                self.board[i] = [(0, 0, 0)] * self.width  # закрашиваем её
                for _ in range(len(self.board) - 1, 0, -1):
                    if _ <= i:  # все ряды выше опускаем
                        self.board[_] = self.board[_ - 1]
                return True
        return False



