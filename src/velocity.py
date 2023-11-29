'''
class for the velocity visualization
'''

import pygame
import sys

class Velocity:
    def __init__(self, screen):
        self.screen = screen
    
    def getData(self):
        # get the data from the other files
        pass

    def update(self):
        self.speed(125)

    def speed(self, speed):
        # draw the text in the middle of the screen
        font = pygame.font.Font('assets/fonts/Seven_Segment.ttf', 65)
        text = font.render(str(speed), False, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (400, 240)
        self.screen.blit(text, textRect)

        # draw the text under changing text which says "km/h"
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("km/h", False, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (400, 280)
        self.screen.blit(text, textRect)
