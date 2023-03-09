import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the ball properties
ball_radius = 50
ball_size = (100, 100)
ball_color = (100, 255, 100)
ball_x = (screen_width // 2) - ball_radius
ball_y = (screen_height // 2) - ball_radius

# Set the ball movement speed
ball_speed = 40

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Set the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= ball_speed
                if ball_y < ball_radius:
                    ball_y = ball_radius
            elif event.key == pygame.K_DOWN:
                ball_y += ball_speed
                if ball_y > screen_height - ball_radius:
                    ball_y = screen_height - ball_radius
            elif event.key == pygame.K_LEFT:
                ball_x -= ball_speed
                if ball_x < ball_radius:
                    ball_x = ball_radius
            elif event.key == pygame.K_RIGHT:
                ball_x += ball_speed
                if ball_x > screen_width - ball_radius:
                    ball_x = screen_width - ball_radius

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
