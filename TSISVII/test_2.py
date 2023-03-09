import pygame
import datetime
import math

# Initialize Pygame
pygame.init()

# Set up the clock face parameters
clock_size = (400, 400)
clock_center = (200, 200)
clock_radius = 180
minute_hand_length = 140
second_hand_length = 160
hand_thickness = 8

# Define a function to convert an angle in degrees to radians
def deg_to_rad(deg):
    return deg * math.pi / 180.0

# Define a function to rotate a point around a pivot
def rotate_point(point, pivot, angle):
    # Translate point so that pivot is at origin
    x = point[0] - pivot[0]
    y = point[1] - pivot[1]

    # Rotate point
    x_new = x * math.cos(angle) - y * math.sin(angle)
    y_new = x * math.sin(angle) + y * math.cos(angle)

    # Translate point back to its original position
    x_new += pivot[0]
    y_new += pivot[1]

    return int(x_new), int(y_new)

# Set up the Pygame display
screen = pygame.display.set_mode(clock_size)

# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the current time
    current_time = datetime.datetime.now()

    # Calculate the rotation angle for the minute hand (in degrees)
    minute_angle = (current_time.minute * 6) + (current_time.second * 0.1)

    # Calculate the rotation angle for the second hand (in degrees)
    second_angle = current_time.second * 6

    # Calculate the endpoints of the minute hand
    minute_hand_end = rotate_point((clock_center[0], clock_center[1] - minute_hand_length), clock_center, deg_to_rad(-minute_angle))

    # Calculate the endpoints of the second hand
    second_hand_end = rotate_point((clock_center[0], clock_center[1] - second_hand_length), clock_center, deg_to_rad(-second_angle))

    # Draw the minute hand
    pygame.draw.line(screen, (255, 0, 0), clock_center, minute_hand_end, hand_thickness)

    # Draw the second hand
    pygame.draw.line(screen, (0, 255, 0), clock_center, second_hand_end, hand_thickness)

    # Draw the clock face
    pygame.draw.circle(screen, (0, 0, 0), clock_center, clock_radius, 4)

    # Update the screen
    pygame.display.flip()

    # Wait for one second
    pygame.time.wait(1000)

