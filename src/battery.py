'''
class for the battery visualization
'''

import pygame
import sys

class Battery:
    def __init__(self, screen):
        self.screen = screen
    
    def getData(self):
        # get the data from the other files
        pass

    def update(self):
        self.battery(50)

    # draw a bar which shows the battery percentage on the left side of the display with a space of 10px to the border
    def battery(self, percentage):
        # check if the percentage is bigger than 100 or smaller than 0
        if percentage > 100:
            percentage = 100
        elif percentage < 0:
            percentage = 0
        # draw the battery
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 30), 3)
        pygame.draw.rect(self.screen, (0, 0, 0), (60, 20, 10, 10))
        pygame.draw.rect(self.screen, (0, 0, 0), (60, 15, 10, 20))
        pygame.draw.rect(self.screen, (0, 0, 0), (70, 25, 10, 0 - percentage * 0.2))
        # draw the percentage
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(str(percentage) + '%', True, (0, 0, 0))
        self.screen.blit(text, (80, 10))
        # draw the border
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 30), 3)
        # draw the text
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('Battery', True, (0, 0, 0))
        self.screen.blit(text, (10, 50))
        # draw the border
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 10, 50, 30), 3)
