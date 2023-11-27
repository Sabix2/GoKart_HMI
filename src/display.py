'''
class for the Display changes
'''

import pygame
import sys

class Display:
    def __init__(self, screen):
        self.screen = screen

    def getData(self):
        # get the data from the other files
        pass

    def update(self):
        self.close_Button()
        self.velocity(0)

    # function to draw the button to close the window on the top right
    def close_Button(self):
        # draw the button
        pygame.draw.rect(self.screen, (255, 0, 0), (760, 0, 40, 40))
        # draw the x
        pygame.draw.line(self.screen, (0, 0, 0), (770, 10), (790, 30), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (770, 30), (790, 10), 5)
        # check if the mouse is over the button
        mouse = pygame.mouse.get_pos()
        if mouse[0] > 760 and mouse[0] < 800 and mouse[1] > 0 and mouse[1] < 40:
            # check if the button is clicked
            if pygame.mouse.get_pressed()[0] == 1:
                # close the window
                pygame.quit()
                sys.exit()
    
    def velocity(self, velocity):
        # draw the text
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Velocity: ' + str(velocity), True, (0, 0, 0))
        self.screen.blit(text, (0, 0))