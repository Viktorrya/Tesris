import pygame

shapes = [[[150, 0], [50, 0], [50, -50], [100, -50], [100, 0], [150, 0], [150, 50], [0, 50]],
          [[150, 0], [200, 0], [200, 50], [0, 50]],
          [[150, -50], [50, 0], [50, 50], [150, 50], [150, 100], [0, 100]],
          [[200, -50], [100, 0], [100, 100], [0, 100]]]
colors = [(255, 186, 0), (226, 139, 0), (241, 58, 19), (127, 143, 24)]


class Shape:
    def __init__(self, count):
        self.color = colors[count % 4]
        self.shape = shapes[count % 4]
        self.a = []

    def render(self, screen):
        self.a = [self.shape[0]]
        for i in range(len(self.shape)):
            if i > 0:
                self.a.append([self.shape[i][0] + self.shape[0][0],
                          self.shape[i][1] + self.shape[0][1]])
        pygame.draw.polygon(screen, self.color, self.a)

    def move(self, screen):
        self.shape[0][1] += 50
        self.render(screen)

    def click(self, pos, screen):
        left = min(list(map(lambda x: x[0], self.a)))
        right = max(list(map(lambda x: x[0], self.a)))
        if pos[0] < left:
            self.shape[0][0] -= 50
        if pos[0] > right:
            self.shape[0][0] += 50
        self.render(screen)