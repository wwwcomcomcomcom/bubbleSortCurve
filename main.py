import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
arrayLength = 800
barWidth = width / arrayLength
barHeightRate = height / arrayLength
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithm Visualization")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Generate random list of numbers
running = True
numbers = [barHeightRate * index for index in range(arrayLength)]
n = len(numbers)
random.shuffle(numbers)
# Main game loop
running = True
clock = pygame.time.Clock()


def render():
    # Clear the screen
    screen.fill(BLACK)

    # Draw the bars
    for i, num in enumerate(numbers):
        pygame.draw.rect(screen, WHITE, (i * barWidth, height - num, barWidth, num))


def renderLine(t):
    for x in range(n):
        if x < n - t:
            drawPoint(x * width / n, height - (x / (x + t + 0.0001)) * height, YELLOW)


def drawPoint(x, y, color):
    pygame.draw.circle(screen, color, (x, y), 2)


# Bubble sort algorithm
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     render()

i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if i < n:
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        render()
        renderLine(i)
        pygame.display.flip()
        clock.tick(15)
        i += 1

# Quit Pygame
pygame.quit()
