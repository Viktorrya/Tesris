import pygame
import os

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


all_sprites = pygame.sprite.Group()


class Shape:
    def __init__(self, count):
        border = pygame.sprite.Sprite()
        border.image = pygame.Surface([500, 1])
        border.rect = border.image.get_rect()
        border.rect.x, border.rect.y = 5, 750
        all_sprites.add(border)
        self.moving_sprite = Moving_shape(count, border)

    def render(self, screen):
        all_sprites.draw(screen)
        sprite = pygame.sprite.Group()
        sprite.add(self.moving_sprite)
        sprite.draw(screen)

    def move(self, screen):
        self.moving_sprite.update()
        self.render(screen)

    def click(self, key, screen):
        if key == pygame.K_RIGHT and self.moving_sprite.rect.x <= 450:
            self.moving_sprite.rect.x += 50
        elif key == pygame.K_LEFT and self.moving_sprite.rect.x >= 50:
            self.moving_sprite.rect.x -= 50
        self.render(screen)

    def ckeck_collid(self, screen):
        if self.moving_sprite.rect.bottom == 800:
            self.render(screen)
            return True
        return False


class Moving_shape(pygame.sprite.Sprite):
    def __init__(self, count, border):
        super().__init__(all_sprites)
        size = sizes[count % 4]
        self.border = border
        self.image = load_image(str(count % 4 + 1) + '.png', size)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = 200, 0

    def update(self):
        if not pygame.sprite.collide_mask(self, self.border):
            self.rect = self.rect.move(0, 50)
        return True