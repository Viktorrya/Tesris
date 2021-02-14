import pygame
import copy

shapes = [[[0, 5], [1, 5], [2, 5], [3, 5]],
          [[0, 4], [0, 5], [0, 6], [1, 5]],
          [[0, 5], [1, 5], [2, 5], [2, 6]]]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


class Shape:
    def __init__(self, count, board):
        a = copy.deepcopy(shapes)
        for i in shapes:
            a.append(i)
        self.coords = a[count % len(shapes)]
        self.color = colors[count % len(colors)]
        self.render(board)

    def check_collid(self, board):
        for i in self.coords:
            if i[0] == 15 or (board.board[i[0] + 1][i[1]] !=
                              (0, 0, 0) and [i[0] + 1, i[1]] not in self.coords):
                return True
        return False

    def move(self, board):
        for i in self.coords:
            board.board[i[0]][i[1]] = (0, 0, 0)
        for i in self.coords:
            i[0] += 1
        self.render(board)

    def render(self, board):
        for i in self.coords:
            board.board[i[0]][i[1]] = self.color

    def click(self, key, board):
        for i in self.coords:
            board.board[i[0]][i[1]] = (0, 0, 0)
        if key == pygame.K_RIGHT:
            a = True
            for i in self.coords:
                if i[1] > 8:
                    a = False
            if not (board.board[i[0]][i[1] + 1] != (0, 0, 0) and
                    [i[0], i[1] + 1] not in self.coords) and a:
                for i in self.coords:
                    i[1] += 1
        elif key == pygame.K_LEFT:
            a = True
            for i in self.coords:
                if i[1] < 1:
                    a = False
            if not (board.board[i[0]][i[1] - 1] != (0, 0, 0) and
                    [i[0], i[1] - 1] not in self.coords) and a:
                for i in self.coords:
                    i[1] -= 1
        elif key == pygame.K_DOWN:
            a = True
            while a:
                self.move(board)
                a = not self.check_collid(board)
        elif key == pygame.K_SPACE:
            y = self.coords[0][0]
            x = self.coords[0][1]
            try:
                if not(board.board[y + i[1] - x][x + i[0] - y] != (0, 0, 0) and
                       [y + i[1] - x, x + i[0] - y] not in self.coords):
                    for i in self.coords:
                        i[0], i[1] = y + i[1] - x, x + i[0] - y
            except(Exception):
                pass
        self.render(board)
