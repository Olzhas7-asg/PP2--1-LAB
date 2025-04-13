import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 400
LANE_WIDTH = ROAD_WIDTH // 2

# Colors
TEXT_COLOR = (255, 255, 255)

# FPS
FPS = 60

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 36)

# Load images
road_image = pygame.image.load("road.jpg")
road_image = pygame.transform.scale(road_image, (ROAD_WIDTH, HEIGHT))
player_image = pygame.image.load("Player.jpg")
player_image = pygame.transform.scale(player_image, (50, 100))
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (50, 100))
enemy_image = pygame.transform.rotate(enemy_image, 180)
coin_image = pygame.image.load("coin.jpg")
coin_image = pygame.transform.scale(coin_image, (30, 30))
police_image = pygame.image.load("police3.jpg")
police_image = pygame.transform.scale(police_image, (60, 120))

# Sounds
coin_sound = pygame.mixer.Sound("coin-song.mp3")
crash_sound = pygame.mixer.Sound("zvuk-avariya-avto.mp3")
pygame.mixer.music.load("48bb90af8e1e401.mp3")
pygame.mixer.music.play(-1)

# Player car
player_pos = [WIDTH // 2 - 25, HEIGHT - 150]
car_speed = 5

# Enemy cars
enemy_cars = []
enemy_spawn_timer = 0
enemy_spawn_interval = 100  # Frames

# Police cars
police_cars = []
police_spawn_timer = 0
police_spawn_interval = 300  # Frames

# Coins
coins = []
coin_weights = [1, 2, 3]  # Different weights for coins
coin_spawn_timer = 0
coin_spawn_interval = 120  # Frames
player_coins = 0

# Function to draw the road
def draw_road():
    screen.blit(road_image, ((WIDTH - ROAD_WIDTH) // 2, 0))

# Function to draw text on the screen
def draw_text(text, x, y):
    label = font.render(text, True, TEXT_COLOR)
    screen.blit(label, (x, y))

# Function to handle game over
def game_over():
    pygame.mixer.music.stop()
    crash_sound.play()
    draw_text("Game Over!", WIDTH // 2 - 100, HEIGHT // 2)
    draw_text(f"Your Score: {player_coins}", WIDTH // 2 - 100, HEIGHT // 2 + 40)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

running = True
while running:
    screen.fill((0, 0, 0))
    draw_road()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_pos[0] > (WIDTH - ROAD_WIDTH) // 2:
        player_pos[0] -= car_speed
    if keys[pygame.K_d] and player_pos[0] < (WIDTH + ROAD_WIDTH) // 2 - 50:
        player_pos[0] += car_speed
    if keys[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= car_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - 100:
        player_pos[1] += car_speed

    # Spawn enemy cars
    enemy_spawn_timer += 1
    if enemy_spawn_timer >= enemy_spawn_interval:
        lane = random.choice([-(LANE_WIDTH // 2), LANE_WIDTH // 2])
        x = WIDTH // 2 + lane
        y = -100
        enemy_cars.append([x, y])
        enemy_spawn_timer = 0

    # Move enemy cars and check for collision
    for enemy in enemy_cars[:]:
        enemy[1] += car_speed
        if (player_pos[0] < enemy[0] + 50 and player_pos[0] + 50 > enemy[0] and
            player_pos[1] < enemy[1] + 100 and player_pos[1] + 100 > enemy[1]):
            game_over()
        if enemy[1] > HEIGHT:
            enemy_cars.remove(enemy)

    # Spawn police cars
    police_spawn_timer += 1
    if police_spawn_timer >= police_spawn_interval:
        lane = random.choice([-(LANE_WIDTH // 2), LANE_WIDTH // 2])
        x = WIDTH // 2 + lane
        y = -120
        police_cars.append([x, y])
        police_spawn_timer = 0

    # Move police cars and check for collision
    for police in police_cars[:]:
        police[1] += car_speed
        if (player_pos[0] < police[0] + 60 and player_pos[0] + 50 > police[0] and
            player_pos[1] < police[1] + 120 and player_pos[1] + 100 > police[1]):
            game_over()
        if police[1] > HEIGHT:
            police_cars.remove(police)

    # Spawn coins
    coin_spawn_timer += 1
    if coin_spawn_timer >= coin_spawn_interval:
        lane = random.choice([-(LANE_WIDTH // 2), LANE_WIDTH // 2])
        x = WIDTH // 2 + lane
        y = -30
        weight = random.choice(coin_weights)
        coins.append([x, y, weight])
        coin_spawn_timer = 0

    # Move and collect coins
    for coin in coins[:]:
        coin[1] += car_speed
        if (player_pos[0] < coin[0] + 30 and player_pos[0] + 50 > coin[0] and
            player_pos[1] < coin[1] + 30 and player_pos[1] + 100 > coin[1]):
            player_coins += coin[2]
            coins.remove(coin)
            coin_sound.play()
        elif coin[1] > HEIGHT:
            coins.remove(coin)

    # Draw elements
    for enemy in enemy_cars:
        screen.blit(enemy_image, (enemy[0], enemy[1]))
    for police in police_cars:
        screen.blit(police_image, (police[0], police[1]))
    for coin in coins:
        screen.blit(coin_image, (coin[0], coin[1]))
    screen.blit(player_image, player_pos)
    draw_text(f"Coins: {player_coins}", 20, 20)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
