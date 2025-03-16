import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

running = True

while running:
    screen.fill((255, 255, 255))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_radius - 20 >= 0:
                ball_y -= 20
            elif event.key == pygame.K_DOWN and ball_y + ball_radius + 20 <= HEIGHT:
                ball_y += 20
            elif event.key == pygame.K_LEFT and ball_x - ball_radius - 20 >= 0:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT and ball_x + ball_radius + 20 <= WIDTH:
                ball_x += 20

    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)  
    pygame.display.flip()

pygame.quit()
