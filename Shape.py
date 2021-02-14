import pygame
import copy
import random
from Consts import shapes, colors


class Shape:
    def __init__(self, board):
        a = copy.deepcopy(shapes)  # позаботимся о том, чтобы список оставался неизменным
        self.coords = random.choices(a, k=1)[0]  # координаты клеток, которые занимает фигура
        self.color = random.choices(colors, k=1)[0]
        self.render(board)

    def check_collid(self, board):
        for i in self.coords:  # если фигура находится в самом низу, или клетка прямо под ней занята
            if i[0] == 15 or (board.board[i[0] + 1][i[1]] !=
                              (0, 0, 0) and [i[0] + 1, i[1]] not in self.coords):
                return True  # то столкновение возвращает тру
        return False

    def move(self, board):
        for i in self.coords:  # сначала стираем место где была фигура ральше
            board.board[i[0]][i[1]] = (0, 0, 0)
        for i in self.coords:
            i[0] += 1  # изменяем координаты
        self.render(board)  # отрисовываем заново

    def render(self, board):
        for i in self.coords:
            board.board[i[0]][i[1]] = self.color

    def click(self, key, board):
        for i in self.coords:
            board.board[i[0]][i[1]] = (0, 0, 0)  # стираем
        if key == pygame.K_RIGHT:
            a = True
            for i in self.coords:
                if i[1] > 8:
                    a = False
            if a:
                if not (board.board[i[0]][i[1] + 1] != (0, 0, 0) and
                        [i[0], i[1] + 1] not in self.coords):
                    for i in self.coords:
                        i[1] += 1  # движение вправо
        elif key == pygame.K_LEFT:
            a = True
            for i in self.coords:
                if i[1] < 1:
                    a = False
            if a:
                if not (board.board[i[0]][i[1] - 1] != (0, 0, 0) and
                        [i[0], i[1] - 1] not in self.coords):
                    for i in self.coords:
                        i[1] -= 1  # движение влево
        elif key == pygame.K_DOWN:
            a = True
            while a:
                self.move(board)  # ускорение фигуры
                a = not self.check_collid(board)
        elif key == pygame.K_SPACE:
            y = self.coords[0][0]
            x = self.coords[0][1]
            try:  # переворот
                if not(board.board[y + i[1] - x][x + i[0] - y] != (0, 0, 0) and
                       [y + i[1] - x, x + i[0] - y] not in self.coords):
                    for i in self.coords:
                        i[0], i[1] = y + i[1] - x, x + i[0] - y
            except(Exception):
                pass
        self.render(board)
