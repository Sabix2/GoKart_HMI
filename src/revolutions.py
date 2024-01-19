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
        self.revBar(2500)

    #function to draw an image which is the background of the revs gauge
    def revsBackground(self):
        #load the image
        image = pygame.image.load("./assets/images/RevsGaugeNew.png")

        #scale the image to 400x400
        image = pygame.transform.scale(image, (400, 400))

        #blit the image to the screen
        self.screen.blit(image, (200, 60))
    
    #function to draw the revs bar using an image which is located in assets/images/RevsGaugeNewOverlay.png
    #the image is 900x900 and has a transparent background
    #the image is beeing cut of by a rectangle which is calculated according to the current revs
    def revBar(self, revs):
        #load the image
        image = pygame.image.load("./assets/images/RevsGaugeNewOverlay.png")

        #scale the image to 400x400
        image = pygame.transform.scale(image, (400, 400))

        #calculate the lenght of the rectangle which is beeing cut of
        #the lenght is calculated according to the current revs
        #the revs range from 0-5500
        rect = pygame.Rect(0, 0, 400, 400)

        #rotatate the rectangel

        #blit the image to the screen
        self.screen.blit(image, (200, 60))