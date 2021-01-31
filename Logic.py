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
        if play:
            shape.move(screen)
        pygame.display.flip()
    pygame.quit()