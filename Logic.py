import pygame
from Board import Board
from Shape import Shape

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tetris')
    size = width, height = 500, 800
    screen = pygame.display.set_mode(size)
    board = Board()
    board.render(screen)
    count = 0
    play = False
    count_of_shapes = 0
    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:
                if count == 0:
                    count = 1
                    play = True
                    shape = Shape(count_of_shapes)
                elif event.type == pygame.KEYDOWN:
                    shape.click(event.key, screen)
        screen.fill((0, 0, 0))
        board.render(screen)
        if not play:
            font = pygame.font.Font('Tetris.ttf', 70)
            text = font.render("Tetris", True, (100, 255, 100))
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
        if play:
            shape.move(screen)
            if shape.ckeck_collid(screen):
                count_of_shapes += 1
                shape = Shape(count_of_shapes)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()