'''
class for the revs of the motor calculations
angle of the arc is 217 degrees
min angle of the arc is at -32 degrees on the left side
max angle of the arc is at -5 degrees on the right side
'''

import pygame
from src.data import Data
from PIL import Image, ImageDraw

class Revolutions:
    def __init__(self, screen):
        self.screen = screen
        self.revs = Data().revs
        self.maxRevs = Data().maxRevs

    def update(self):
        self.revsBackground()
        self.revBar(self.revs)

    #function to draw an image which is the background of the revs gauge
    def revsBackground(self):
        #load the image
        image = pygame.image.load("./assets/images/RevsGauge.png")
        #blit the image to the screen
        self.screen.blit(image, (200, 60))
    
    #function to draw the revs bar using an image which is located in assets/images/RevsGaugeNewOverlay.png
    #the image is beeing cut of by a rectangle which is calculated according to the current revs
    def revBar(self, revs):
        angle = self.calc_angle(revs)

        if angle != 0:
            cutimg = self.cut_gauge_sector_from_image(angle)

            #convert the image to pygame
            mode = cutimg.mode
            size = cutimg.size
            data = cutimg.tobytes()
            img = pygame.image.fromstring(data, size, mode)
            rect = img.get_rect()
            rect.center = 400, 260

            self.screen.blit(img, rect)
        else:
            self.screen.blit(pygame.image.load("./assets/images/RevsGaugeOverlay.png"), (200, 60))

    def cut_gauge_sector_from_image(self, angle):
        min_angle = 0

        # Open the image
        img = Image.open('./assets/images/RevsGaugeOverlay.png')

        # Create a mask based on the angle
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)

        draw.pieslice([(0, 0), img.size], min_angle, -angle, fill=255)

        # Apply the mask to the image
        result = Image.new('RGBA', img.size, (255, 255, 255, 0))
        result.paste(img, mask=mask)
        return result
    
    #min 0 max 207
    # 0 ... full gauge
    # 207 ... empty gauge
    def calc_angle(self, revs):
        angle = 207 - (207 / self.maxRevs) * revs
        return angle