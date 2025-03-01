import pygame
import time
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)

# Load images
background = pygame.image.load("mickeyclock/mickeyclock.jpeg")  # Load your clock face image
minute_hand = pygame.image.load("mickeyclock/right.png")  # Load Mickey's right hand (minutes)
second_hand = pygame.image.load("mickeyclock/left/left.png")  # Load Mickey's left hand (seconds)

# Scale hands appropriately
minute_hand = pygame.transform.scale(minute_hand, (200, 20))
second_hand = pygame.transform.scale(second_hand, (200, 20))

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Get current time
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate rotation angles
    minute_angle = -(minutes * 6)  # 360 degrees / 60 minutes = 6 degrees per minute
    second_angle = -(seconds * 6)  # 360 degrees / 60 seconds = 6 degrees per second

    # Rotate hands
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    # Get new rects and position them at the center
    minute_rect = rotated_minute.get_rect(center=CENTER)
    second_rect = rotated_second.get_rect(center=CENTER)

    # Draw hands
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1)  # Update every second

pygame.quit()