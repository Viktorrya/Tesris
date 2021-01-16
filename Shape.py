import pygame

shapes = [((150, 0), (200, 0), (200, -50), (250, -50), (250, 0), (300, 0), (300, 50), (150, 50)),
          ((150, 0), (350, 0), (350, 50), (150, 50)),
          ((150, -50), (200, -50), (200, 0), (300, 0), (300, 50), (150, 50)),
          ((200, -50), (300, -50), (30, 50), (200, 50))]
colors = [(255, 186, 0), (226, 139, 0), (241, 58, 19), (127, 143, 24)]


class Shape:
    def __init__(self, count):
        self.color = colors[count % 4]
        self.shape = shapes[count % 4]

    def render(self, screen):
        pygame.draw.polygon(screen, self.color, self.shape)
        c = tuple(map(lambda x: x // 2, self.color))
        pygame.draw.polygon(screen, c, self.shape, 1)

    def move(self, screen):
        self.shape = tuple(map(lambda x: (x[0], x[1] + 10), self.shape))
        self.render(screen)

    def click(self, pos, screen):
        left = min(list(map(lambda x: x[0], self.shape)))
        right = max(list(map(lambda x: x[0], self.shape)))
        if pos[0] < left:
            self.shape = tuple(map(lambda x: (x[0] - 50, x[1]), self.shape))
        if pos[0] > right:
            self.shape = tuple(map(lambda x: (x[0] + 50, x[1]), self.shape))
        self.render(screen)