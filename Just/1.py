import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and Food Initialization
snake = [(WIDTH // 2, HEIGHT // 2)]  # Snake starts at the center
direction = RIGHT
food = (0, 0)

# Score and Level
score = 0
level = 1
speed = FPS


# Generate Food avoiding Snake and Borders
def generate_food():
    while True:
        x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        if (x, y) not in snake:
            return x, y


food = generate_food()

# Game Loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(speed)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Move Snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0] * CELL_SIZE, head_y + direction[1] * CELL_SIZE)

    # Check for wall collision
    if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False  # Game over if hitting the wall

    # Check for self collision
    if new_head in snake:
        running = False  # Game over if collides with itself

    # Add new head to Snake
    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        score += 1
        food = generate_food()

        # Level up every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2  # Increase speed
    else:
        snake.pop()  # Remove tail to keep Snake length

    # Draw everything
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Display Score and Level
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
