'''
main file
a 800x480 display
displays the current velocity of the Gokart
displays the current battery voltage
displays the current errors
displays the current revolutions per minute of the motor
displays the current mode selected
'''

# imports
import pygame

# local imports
from src.display import Display

# innit pygame
pygame.init()

# set up the pygame window
#                                           change to NOFRAME for linux
screen = pygame.display.set_mode((800, 480), pygame.SHOWN)

# set up the instances of the classes
Frame = Display(screen)

# set up the pygame loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a dark grey
    screen.fill((40, 40, 40))

    # make the display update
    Frame.update()

    # update the display
    pygame.display.flip()

# end of the program