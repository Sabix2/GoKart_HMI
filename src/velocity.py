'''
class for the velocity visualization
'''

import pygame
from src.data import Data

class Velocity:
    def __init__(self, screen):
        self.screen = screen
        self.velocity = Data().velocity

    def update(self):
        self.speed(self.velocity)

    def speed(self, speed):
        # draw the text in the middle of the screen
        font = pygame.font.Font('assets/fonts/Seven_Segment.ttf', 65)
        text = font.render(str(speed), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (400, 240)
        self.screen.blit(text, textRect)

        # draw the text under changing text which says "km/h"
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("km/h", False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (400, 280)
        self.screen.blit(text, textRect)
