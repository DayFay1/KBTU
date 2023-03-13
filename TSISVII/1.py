import pygame
import time
import urllib.request

url = "https://raw.githubusercontent.com/arnee99/Spring-PP2/main/Assignment%207/images/mickeyclock.jpeg"
filename = "mickey.png"

urllib.request.urlretrieve(url, filename)

pygame.init()

# Set up the window
size = width, height = 400, 400
screen = pygame.display.set_mode(size)

# Load Mickey image
mickey = pygame.image.load(filename)

# Define the rotation angles for the hands
minute_angle = -90
second_angle = -90

# Run the clock
while True:
    # Get the current time
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate the rotation angles for the hands
    minute_angle = -90 + minute * 6
    second_angle = -90 + second * 6

    # Rotate the hands
    minute_hand = pygame.transform.rotate(mickey, minute_angle)
    second_hand = pygame.transform.rotate(mickey, second_angle)

    # Draw the clock face
    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))

    # Draw the hands
    screen.blit(minute_hand, (0, 0))
    screen.blit(second_hand, (0, 0))

    # Update the display
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
