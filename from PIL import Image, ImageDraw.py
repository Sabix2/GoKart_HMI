from PIL import Image, ImageDraw
import pygame
import time

#min -213
#max 5
#maxmax 6
def cut_gauge_sector_from_image(image_path, angle):
    min_angle = 6

    # Open the image
    img = Image.open(image_path)

    # Create a mask based on the angle
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)

    draw.pieslice([(0, 0), img.size], min_angle, angle, fill=255)

    # Apply the mask to the image
    result = Image.new('RGBA', img.size, (255, 255, 255, 0))
    result.paste(img, mask=mask)
    return result

""" # Example usage:
image_path = './assets/images/RevsGaugeNewOverlay.png'
angle_to_cut = 5
cut_gauge_sector_from_image(image_path, angle_to_cut) """

# main function for a pygame window, which shows the cut image
def main():
    # Initialize the pygame
    pygame.init()
    # Set the dimensions of the window
    width = 400
    height = 400
    # Create the window
    screen = pygame.display.set_mode((width, height))

    # Set the angle to cut
    angle_to_cut = 5

    image_path = './assets/images/RevsGaugeNewOverlay.png'

    # Cut the sector from the image
    cutimg = cut_gauge_sector_from_image(image_path, angle_to_cut)

    mode = cutimg.mode
    size = cutimg.size
    data = cutimg.tobytes()
    #import image to pygame
    img = pygame.image.fromstring(data, size, mode)
    rect = img.get_rect() 
    rect.center = width//2, height//2

    # Run the game loop
    running = True
    while running:
        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Cut the sector from the image
        cutimg = cut_gauge_sector_from_image(image_path, angle_to_cut)

        mode = cutimg.mode
        size = cutimg.size
        data = cutimg.tobytes()
        #import image to pygame
        img = pygame.image.fromstring(data, size, mode)
        rect = img.get_rect() 
        rect.center = width//2, height//2

        # Draw the image
        screen.blit(img, rect)

        # Update the display
        pygame.display.flip()

        angle_to_cut -= 1
        time.sleep(0.05)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit the game
    pygame.quit()

main()