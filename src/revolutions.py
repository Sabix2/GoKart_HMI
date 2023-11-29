'''
class for the revs of the motor calculations
'''

import pygame
import sys
from pygame import gfxdraw

class Revolutions:
    def __init__(self, screen):
        self.screen = screen
        self.maxRevs = 5500
    
    def getData(self):
        # get the data from the other files
        pass

    def update(self):
        self.revBar(5500/2)

    # function to draw the arc bar for the revolutions (rpm)
    # revs range from 0-5500
    def revBar(self, revs):
        # draw the arc, a circle which should have the velocity in the middle of the rect parameter rect parameter should be 400x400 the arc should be 200 degrees with a gap at the bottom of 160 degrees the arc should start at 140 degrees
        pygame.draw.arc(self.screen, (20, 20, 20), (200, 60, 400, 400), -3.14/5.5, 3.14+3.14/5.5, 15)

        # draw the arc of the max revs minus the current revs
        # calculate the angle of the arc, where it should start according to the current revs
        angle = (3.14 + 3.14/2.75)*(revs/self.maxRevs)
        pygame.draw.arc(self.screen, (0, 100, 0), (200, 60, 400, 400), ((3.14+3.14/5.5)-angle), 3.14+3.14/5.5, 15)


