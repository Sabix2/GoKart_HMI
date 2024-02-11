'''
class for the error events
'''

import pygame
from src.data import Data

class Error:
    def __init__(self, screen):
        self.screen = screen
        self.percentage = Data().percentage

    def update(self):
        self.batteryWarning(self.percentage)

    # function to display errors when the battery is normal/low/critical
    def batteryWarning(self, percentage):
        if percentage > 20:
            # display the image for a full battery
            img = pygame.image.load("assets/images/warnings/BatteryWarningStandby.png")
        elif percentage > 10:
            # display the image for a low battery
            img = pygame.image.load("assets/images/warnings/BatteryWarningLow.png")
        else:
            # display the image for a critical battery
            img = pygame.image.load("assets/images/warnings/BatteryWarningCritical.png")

        # scale the image to 50x50
        img = pygame.transform.scale(img, (50, 50))
        # place the image below the battery bar
        self.screen.blit(img, (45, 410))

    def temperatureWarning(self):
        pass

    def collisionWarning(self):
        pass