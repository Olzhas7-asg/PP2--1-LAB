import pygame
import random
import time
import psycopg2
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Функция подключения к базе данных
def connect_db():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# Получение или создание пользователя в базе данных
def get_or_create_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, current_level FROM Users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        cursor.execute(
            "INSERT INTO Users (username, current_level) VALUES (%s, 1) RETURNING id, current_level",
            (username,)
        )
        user = cursor.fetchone()
        print(f"New user created: {username}")
    else:
        print(f"Welcome back, {username}! Current level: {user[1]}")
    conn.commit()
    cursor.close()
    conn.close()
    return user[0], user[1]

# Сохранение очков в базе данных
def save_score(user_id, score, level):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO UserScores (user_id, score) VALUES (%s, %s)",
        (user_id, score)
    )
    cursor.execute(
        "UPDATE Users SET current_level = %s WHERE id = %s",
        (level, user_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Шрифт
font = pygame.font.SysFont("Arial", 24)

# Функции
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def show_text(text, x, y, color=WHITE):
    screen.blit(font.render(text, True, color), (x, y))

def generate_food(snake):
    while True:
        new_food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if new_food not in snake:
            return new_food

# Ввод имени пользователя
username = input("Enter your username: ")
user_id, level = get_or_create_user(username)

# Инициализация змейки и еды
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (CELL_SIZE, 0)
food = None
score = 0
speed = FPS + (level - 1) * 2

# Игровой цикл
running = True
paused = False
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Пауза игры
                paused = not paused
            if event.key == pygame.K_q:  # Выход и сохранение
                save_score(user_id, score, level)
                running = False

    if paused:
        show_text("Game Paused. Press 'P' to resume.", WIDTH // 2 - 150, HEIGHT // 2, WHITE)
        pygame.display.flip()
        continue

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Движение змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]

    # Проверка столкновения со стенами
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False

    # Проверка столкновения с самой собой
    if new_head in snake[1:]:
        running = False

    # Появление еды, если ее нет
    if not food:
        food = generate_food(snake)

    # Проверка, съела ли змейка еду
    if new_head == food:
        snake.append(snake[-1])  # Растет змейка
        score += 1
        food = None

        # Повышение уровня
        if score % 10 == 0:
            level += 1
            speed += 2

    # Отображение
    draw_snake(snake)
    if food:
        draw_food(food)
    show_text(f"Score: {score}", 10, 10)
    show_text(f"Level: {level}", 10, 40)

    pygame.display.flip()
    clock.tick(speed)

# Сообщение об окончании игры
screen.fill(BLACK)
show_text(f"Game Over! Your score is: {score}", WIDTH // 2 - 150, HEIGHT // 2, RED)
pygame.display.flip()
time.sleep(3)

pygame.quit()

