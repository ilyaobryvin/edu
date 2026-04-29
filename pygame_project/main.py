import pygame
import random
import time


pygame.init()

# Определяем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры экрана
WIDTH = 600
HEIGHT = 400

# Размер одного блока змейки
BLOCK_SIZE = 20

# Установка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')

# Установка времени обновления игры
clock = pygame.time.Clock()
SNAKE_SPEED = 15

# Шрифт для отображения текста
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция отображения счета
def display_score(score):
    value = score_font.render("Счет: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Функция отображения сообщения
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Основная игра
def game_loop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x = WIDTH / 2
    y = HEIGHT / 2

    # Направление змейки
    x_change = 0
    y_change = 0

    # Тело змейки
    snake = []
    snake_length = 1

    # Координаты еды
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Основной цикл игры
    while not game_over:

        while game_close:
            screen.fill(BLUE)
            display_message("Проигрыш! Нажмите Q - выйти или C - играть снова", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обработка нажатий клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Обновление положения змейки
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change

        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Обновление тела змейки
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        # Проверка на столкновение с самим собой
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        # Рисуем змейку
        for segment in snake:
            pygame.draw.rect(screen, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        display_score(snake_length - 1)

        pygame.display.update()

        # Если змейка съела еду
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        # Устанавливаем скорость игры
        clock.tick(SNAKE_SPEED)

    # Завершаем работу pygame
    pygame.quit()
    quit()

# Запуск игры
game_loop()