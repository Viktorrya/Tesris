import os, sys
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
        self.rect.x = self.rect.x + 1


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def humans_when_defeat(screen):
    running = True
    fps = 100
    clock = pygame.time.Clock()
    sprite = Sprite_humans()
    all_sprites.add(sprite)
    while running:
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        sprite.update()
        if sprite.rect.x == 0:
            running = False
        clock.tick(fps)
        pygame.display.flip()
    sprite.kill()

