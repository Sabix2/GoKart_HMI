'''
class for the revs of the motor calculations
angle of the arc is 217 degrees
min angle of the arc is at -32 degrees on the left side
max angle of the arc is at -5 degrees on the right side
'''

import pygame
from src.data import Data

class Revolutions:
    def __init__(self, screen):
        self.screen = screen
        self.revs = Data().revs
        self.maxRevs = Data().maxRevs

    def update(self):
        self.revsBackground()
        self.neorevBar(2500)

    #function to draw an image which is the background of the revs gauge
    def revsBackground(self):
        #load the image
        image = pygame.image.load("./assets/images/RevsGaugeNew.png")

        #scale the image to 400x400
        image = pygame.transform.scale(image, (400, 400))

        #blit the image to the screen
        self.screen.blit(image, (200, 60))
    
    #function to draw the revs bar using an image which is located in assets/images/RevsGaugeNewOverlay.png
    #the image is beeing cut of by a rectangle which is calculated according to the current revs
    def revBar(self, revs):
        #load the image
        image = pygame.image.load("./assets/images/RevsGaugeNewOverlay.png")

        #calculate the lenght of the rectangle which is beeing cut of
        #the lenght is calculated according to the current revs
        #the revs range from 0-5500
        rect = pygame.Rect(0, 0, 400, 400)

        #rotatate the rectangel

        #blit the image to the screen
        self.screen.blit(image, (200, 60))

    # create the arc for the revs
    def neorevBar(self, revs):

        # set the position of the arc
        x = 230
        y = 91

        # set the height and width of the arc
        width = 341
        height = 341

        # set the start and end angle of the arc in radians
        start_angle = -0.2
        end_angle = 3.6

        # draw the arc
        pygame.draw.arc(self.screen, (0, 0, 255), (x, y, width, height), start_angle, end_angle, 17)

        # draw the arc
        pygame.draw.arc(self.screen, (0, 0, 250), (x, y, width, height), start_angle, end_angle, 17)