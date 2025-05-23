import pygame
import sys
import tkinter as tk
from tkinter import colorchooser

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TOOLBAR_HEIGHT = 50
BACKGROUND_COLOR = (255, 255, 255)
TOOLBAR_COLOR = (200, 200, 200)
DEFAULT_COLOR = (0, 0, 0)

# Tools
DRAW_RECTANGLE = "rectangle"
DRAW_CIRCLE = "circle"
DRAW_LINE = "line"
DRAW_SQUARE = "square"
DRAW_RIGHT_TRIANGLE = "right_triangle"
DRAW_EQUILATERAL_TRIANGLE = "equilateral_triangle"
DRAW_RHOMBUS = "rhombus"
ERASER = "eraser"

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

# Colors
current_color = DEFAULT_COLOR

tool = DRAW_LINE
start_pos = None
drawing = False

# Toolbar buttons
buttons = {
    "rectangle": pygame.Rect(10, 10, 80, 30),
    "circle": pygame.Rect(100, 10, 80, 30),
    "square": pygame.Rect(190, 10, 80, 30),
    "right_triangle": pygame.Rect(280, 10, 80, 30),
    "equilateral_triangle": pygame.Rect(370, 10, 80, 30),
    "rhombus": pygame.Rect(460, 10, 80, 30),
    "eraser": pygame.Rect(550, 10, 80, 30),
    "color": pygame.Rect(640, 10, 80, 30),
}

def draw_toolbar():
    pygame.draw.rect(screen, TOOLBAR_COLOR, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    for button in buttons.values():
        pygame.draw.rect(screen, (0, 0, 0), button, 2)

    font = pygame.font.SysFont(None, 24)
    screen.blit(font.render("Rect", True, (0, 0, 0)), (20, 15))
    screen.blit(font.render("Circle", True, (0, 0, 0)), (110, 15))
    screen.blit(font.render("Square", True, (0, 0, 0)), (200, 15))
    screen.blit(font.render("R-Tri", True, (0, 0, 0)), (290, 15))
    screen.blit(font.render("E-Tri", True, (0, 0, 0)), (380, 15))
    screen.blit(font.render("Rhomb", True, (0, 0, 0)), (470, 15))
    screen.blit(font.render("Eraser", True, (0, 0, 0)), (560, 15))
    screen.blit(font.render("Color", True, (0, 0, 0)), (650, 15))

def choose_color():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    color_code = colorchooser.askcolor(title="Choose color")
    root.destroy()
    if color_code[0]:
        return tuple(map(int, color_code[0]))
    return current_color

# Main loop
running = True
screen.fill(BACKGROUND_COLOR)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] < TOOLBAR_HEIGHT:
                # Check toolbar buttons
                if buttons["rectangle"].collidepoint(event.pos):
                    tool = DRAW_RECTANGLE
                elif buttons["circle"].collidepoint(event.pos):
                    tool = DRAW_CIRCLE
                elif buttons["square"].collidepoint(event.pos):
                    tool = DRAW_SQUARE
                elif buttons["right_triangle"].collidepoint(event.pos):
                    tool = DRAW_RIGHT_TRIANGLE
                elif buttons["equilateral_triangle"].collidepoint(event.pos):
                    tool = DRAW_EQUILATERAL_TRIANGLE
                elif buttons["rhombus"].collidepoint(event.pos):
                    tool = DRAW_RHOMBUS
                elif buttons["eraser"].collidepoint(event.pos):
                    tool = ERASER
                elif buttons["color"].collidepoint(event.pos):
                    current_color = choose_color()
            else:
                start_pos = event.pos
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos

                if tool == DRAW_RECTANGLE:
                    width = end_pos[0] - start_pos[0]
                    height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], width, height), 2)

                elif tool == DRAW_CIRCLE:
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)

                elif tool == DRAW_SQUARE:
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], side, side), 2)

                elif tool == DRAW_RIGHT_TRIANGLE:
                    pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)

                elif tool == DRAW_EQUILATERAL_TRIANGLE:
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.polygon(screen, current_color, [
                        start_pos,
                        (start_pos[0] + side, start_pos[1]),
                        (start_pos[0] + side // 2, start_pos[1] - int((3**0.5 / 2) * side))
                    ], 2)

                elif tool == DRAW_RHOMBUS:
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, current_color, [
                        (start_pos[0], start_pos[1] - height // 2),
                        (start_pos[0] + width // 2, start_pos[1]),
                        (start_pos[0], start_pos[1] + height // 2),
                        (start_pos[0] - width // 2, start_pos[1])
                    ], 2)

                elif tool == ERASER:
                    width = end_pos[0] - start_pos[0]
                    height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(screen, BACKGROUND_COLOR, (start_pos[0], start_pos[1], width, height))

            start_pos = None
            drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == DRAW_LINE:
                end_pos = event.pos
                pygame.draw.line(screen, current_color, start_pos, end_pos, 2)
                start_pos = end_pos

    draw_toolbar()
    pygame.display.flip()

pygame.quit()
sys.exit()
