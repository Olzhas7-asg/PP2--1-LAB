import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font
font = pygame.font.SysFont("Arial", 24)

# Snake and food
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (CELL_SIZE, 0)
food = None
food_weight = 0
food_spawn_time = 0
score = 0
level = 1
speed = FPS

# Functions
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

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]

    # Check collision with walls
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False

    # Check collision with itself
    if new_head in snake[1:]:
        running = False

    # Spawn food if none exists or if it's been too long
    if food is None or time.time() - food_spawn_time > 5:  # Food disappears after 5 seconds
        food = generate_food(snake)
        food_weight = random.randint(1, 3)  # Random weight for the food
        food_spawn_time = time.time()

    # Check if food is eaten
    if new_head == food:
        snake.append(snake[-1])  # Grow snake
        score += food_weight  # Add food weight to score
        food = None

        # Level up
        if score % 10 == 0:
            level += 1
            speed += 2

    # Draw everything
    draw_snake(snake)
    if food:
        draw_food(food)
    show_text(f"Score: {score}", 10, 10)
    show_text(f"Level: {level}", 10, 40)

    pygame.display.flip()
    clock.tick(speed)

# End message
screen.fill(BLACK)
show_text(f"Game Over! Your score is: {score}", WIDTH // 2 - 150, HEIGHT // 2, RED)
pygame.display.flip()
time.sleep(3)

pygame.quit()
