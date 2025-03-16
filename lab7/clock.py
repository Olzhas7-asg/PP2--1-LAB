import pygame
import datetime
pygame.init()

width, height = 600 , 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("mickey clock")

mickey_face= pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

mickey_face = pygame.transform.scale(mickey_face, (400 , 400))
minute_hand = pygame.transform.scale(minute_hand, (450, 500))
second_hand = pygame.transform.scale(second_hand, (450, 500))

center_x, center_y = width // 2, height // 2

def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=(center_x, center_y))
    return rotated_image, rect

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute_angle = -6 * now.minute 
    second_angle = -6 * now.second  

    screen.blit(mickey_face, (center_x - 200, center_y - 200))

    
    minute_img, minute_rect = rotate_hand(minute_hand, minute_angle)
    second_img, second_rect = rotate_hand(second_hand, second_angle)

    screen.blit(minute_img, minute_rect)
    screen.blit(second_img, second_rect)

    pygame.display.flip()
    clock.tick(60)


