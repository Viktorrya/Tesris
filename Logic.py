import pygame
from Board import Board
from Shape import Shape
import Humans

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Tetris')
    size = width, height = 500, 800
    screen = pygame.display.set_mode(size)
    board = Board()  # создаём поле
    board.render(screen)  # отрисовываем его
    count = 0
    play = False
    fps = 3  # количество кадров в секунду
    clock = pygame.time.Clock()
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:
                if count == 0:  # если игра ещё не начата, достаточно кликнуть мышью
                    count = 1
                    play = True
                    shape = Shape(board)  # создаём первую фигурку
                elif event.type == pygame.KEYDOWN:  # обрабатывает нажатия с клавиатуры
                    shape.click(event.key, board)
        screen.fill((0, 0, 0))
        board.render(screen)
        if not play:  # пока игра не началась, пользователь видит её заставку
            font = pygame.font.Font('Tetris.ttf', 70)
            text = font.render("Tetris", True, (100, 255, 100))
            text_x = width // 2 - text.get_width() // 2
            text_y = height // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
        if play:
            if shape.check_collid(board):  # проверка на столкновение, она означает что фигурка приземлилась
                score += 1  # за каждую успешно опущенную фигурку - 1 балл
                if board.check_line():  # проверка. нет ли заполненых лииний
                    score += 10
                a = shape.coords
                shape = Shape(board)  # создание новой фигуры
                b = False
                print(a, shape. coords)
                for i in shape.coords:
                    if i in a:
                        b = True
                        break
                if b:  # проверка на проигрыш
                    play = False
                    count = 0
                    count_of_shapes = 0
                    screen = pygame.display.set_mode(size)
                    board = Board()
                    board.render(screen)
                    score = 0
                    screen.fill((0, 0, 0))
                    Humans.humans_when_defeat(screen)
            else:
                shape.move(board)  # если препятствий нет, двигаем фигурку
        font = pygame.font.Font('Tetris.ttf', 30)  # отрисовываем значение счёта
        text = font.render(str(score), True, (255, 255, 255))
        text_x = 460
        text_y = 10
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
