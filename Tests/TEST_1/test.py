import pygame
import random

# initialize Pygame
pygame.init()

# set up game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman Game")

# set up colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# set up game variables
pacman_position = [250, 350]
pacman_radius = 15
pacman_speed = 5
food_position = [random.randint(0, WINDOW_WIDTH-10), random.randint(0, WINDOW_HEIGHT-10)]
food_color = YELLOW
food_radius = 10
score = 0

# set up game loop
game_running = True
while game_running:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # move pacman
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and pacman_position[1] > pacman_radius:
        pacman_position[1] -= pacman_speed
    if keys[pygame.K_DOWN] and pacman_position[1] < WINDOW_HEIGHT-pacman_radius:
        pacman_position[1] += pacman_speed
    if keys[pygame.K_LEFT] and pacman_position[0] > pacman_radius:
        pacman_position[0] -= pacman_speed
    if keys[pygame.K_RIGHT] and pacman_position[0] < WINDOW_WIDTH-pacman_radius:
        pacman_position[0] += pacman_speed

    # check if pacman ate the food
    distance = ((pacman_position[0]-food_position[0])**2 + (pacman_position[1]-food_position[1])**2)**0.5
    if distance < pacman_radius + food_radius:
        score += 1
        food_position = [random.randint(0, WINDOW_WIDTH-10), random.randint(0, WINDOW_HEIGHT-10)]

    # draw game objects
    GAME_WINDOW.fill(BLACK)
    pygame.draw.circle(GAME_WINDOW, BLUE, pacman_position, pacman_radius)
    pygame.draw.circle(GAME_WINDOW, food_color, food_position, food_radius)
    pygame.draw.text(GAME_WINDOW, RED, (10, 10), f"Score: {score}", 24)

    # update display
    pygame.display.update()

# quit Pygame
pygame.quit()