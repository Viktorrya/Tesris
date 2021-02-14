import os
import pygame

all_sprites = pygame.sprite.Group()


class Sprite_humans(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        size = (500, 140)
        self.image = load_image('humans.png', size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -500, 300

    def update(self):
        self.rect = self.rect.move(1, 0)


def load_image(name, size, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    image = pygame.transform.scale(image, size)
    return image


def humans_when_defeat(screen):
    running = True
    fps = 30
    clock = pygame.time.Clock()
    sprite = Sprite_humans()
    all_sprites.add(sprite)
    while running:
        all_sprites.draw(screen)
        sprite.update()
        if sprite.rect.x == 500:
            running = False
        clock.tick(fps)


size = width, height = 500, 800
screen = pygame.display.set_mode(size)
humans_when_defeat(screen)