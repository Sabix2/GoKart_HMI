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
        self.batteryBar(25)

    # function to draw a battery bar that gets an input 0-100, the bar should be standing and on the left side
    def batteryBar(self, percentage):
        # draw the background of the battery bar
        pygame.draw.rect(self.screen, (50, 50, 50), (50, 80, 50, 320))
        # draw the battery bar, which changes with the percentage
        pygame.draw.rect(self.screen, (0, 150, 0), (50, 400 - percentage * 3.2, 50, percentage * 3.2))
        # draw the text which shows the percentage below the battery bar
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str(percentage) + "%", False, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (75, 430)
        self.screen.blit(text, textRect)
