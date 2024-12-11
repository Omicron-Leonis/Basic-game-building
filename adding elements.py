import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My first game screen")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Example rectangle color
BLACK = (0, 0, 0)

# Fill the background with white
screen.fill(WHITE)

# Create a rectangle at the center of the screen
rect_width, rect_height = 100, 50
rect_x = (WINDOW_WIDTH - rect_width) // 2
rect_y = (WINDOW_HEIGHT - rect_height) // 2
pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

# Display text on the screen
font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, BLACK)
text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
screen.blit(text, text_rect)

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
