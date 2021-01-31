import pygame
import os, sys

sizes = [(50, 200), (150, 100), (100, 100), (100, 150)]


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


class Shape:
    def __init__(self, count):
        self.shape = (count + 1) % 4
        self.a = []
        self.all_sprites = pygame.sprite.Group()
        self.moving_sprite = pygame.sprite.Sprite()
        size = sizes[(count + 1) % 4]
        self.moving_sprite.image = load_image('2.png', size)
        self.moving_sprite.rect = self.moving_sprite.image.get_rect()
        self.moving_sprite.rect.x, self.moving_sprite.rect.y = 200, 0

    def render(self, screen):
        self.all_sprites.draw(screen)
        sprite = pygame.sprite.Group()
        sprite.add(self.moving_sprite)
        sprite.draw(screen)

    def move(self, screen):
        self.moving_sprite.rect.y += 10
        self.render(screen)

    def click(self, key, screen):
        if key == pygame.K_RIGHT and self.moving_sprite.rect.x <= 450:
            self.moving_sprite.rect.x += 50
        elif key == pygame.K_LEFT and self.moving_sprite.rect.x >= 50:
            self.moving_sprite.rect.x -= 50
        self.render(screen)