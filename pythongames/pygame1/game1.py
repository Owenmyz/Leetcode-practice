import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello Pygame')

# Set up fonts
font = pygame.font.SysFont(None, 55)

# Set up the text
text = font.render('Hello, Everyone', True, (255, 255, 255))
text_rect = text.get_rect(center=(width / 2, height / 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    window.fill((13, 76, 53))

    # Draw the text
    window.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
