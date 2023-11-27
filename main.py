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
import time

# local imports
from src.display import Display
# from src.button import Button
# from src.mode import Mode
# from src.error import Error
# from src.revolutions import Revolutions
# from src.battery import Battery
# from src.velocity import Velocity

# innit pygame
pygame.init()

# set up the pygame window
screen = pygame.display.set_mode((800, 480), pygame.NOFRAME)

# set up the instances of the classes
Frame = Display(screen)
# reverseButton = Button()
# modeButton = Button()
# analyzeButton = Button()
# Error = Error()
# Revolutions = Revolutions()
# Battery = Battery()
# Velocity = Velocity()

# set up the pygame loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with white
    screen.fill((100, 100, 100))

    # make a button to close the window
    Frame.close_Button()

    # update the display
    pygame.display.flip()

# end of the program