import pygame

# Initialize Pygame
pygame.init()

# Set screen size and caption
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Arc Example")

# Set clock and colors
clock = pygame.time.Clock()
blue = (0, 0, 255)
blue1 = (0, 0, 200)
dark_grey = (30, 30, 30)

# Define rectangle for the arc
rect = pygame.Rect(50, 50, 500, 500)

stop = 0
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with dark grey
    screen.fill(dark_grey)

    # Draw the arc with adjusted width and angle
    pygame.draw.arc(screen, blue, rect, 0, stop, 15)  # Starts at right, goes counter-clockwise, width 15
    pygame.draw.arc(screen, blue1, rect, 0, stop, 15)
    
    # Increase the stop angle
    stop += 0.5

    # Update the display
    pygame.display.flip()

    # Set FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
