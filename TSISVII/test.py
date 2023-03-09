import pygame
import datetime

pygame.init()

# Load the image of Mickey Mouse with his hands at 12 o'clock position
clock_face = pygame.image.load("mickey_clock.png")
clock_face_rect = clock_face.get_rect()

# Load the images of Mickey's hands
seconds_hand = pygame.image.load("mickey_seconds.png")
seconds_hand_rect = seconds_hand.get_rect(center=clock_face_rect.center)
minutes_hand = pygame.image.load("mickey_minutes.png")
minutes_hand_rect = minutes_hand.get_rect(center=clock_face_rect.center)

# Define a function to rotate Mickey's hands according to the current time
def update_hands():
    current_time = datetime.datetime.now()
    seconds_angle = current_time.second * 6  # 6 degrees per second
    minutes_angle = current_time.minute * 6 + current_time.second / 10  # 6 degrees per minute, 1 degree per 10 seconds
    seconds_hand_rotated = pygame.transform.rotate(seconds_hand, seconds_angle)
    minutes_hand_rotated = pygame.transform.rotate(minutes_hand, minutes_angle)
    return seconds_hand_rotated, minutes_hand_rotated

# Set up the Pygame display window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")

# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get the current time and rotate Mickey's hands accordingly
    seconds_hand_rotated, minutes_hand_rotated = update_hands()

    # Blit the clock face and hands onto the screen
    screen.blit(clock_face, clock_face_rect)
    screen.blit(seconds_hand_rotated, seconds_hand_rect)
    screen.blit(minutes_hand_rotated, minutes_hand_rect)

    # Update the screen
    pygame.display.update()

    # Wait for one second
    pygame.time.wait(1000)
