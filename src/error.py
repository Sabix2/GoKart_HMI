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

    # function to display an image if the perdcenage of the battery is low and another image if the battery is full
    def batteryWarning(self, percentage):
        if percentage > 20:
            # display the image for a full battery
            img = pygame.image.load("assets/images/BatteryWarningStandby.png")
        elif percentage > 10:
            # display the image for a low battery
            img = pygame.image.load("assets/images/BatteryWarningLow.png")
        else:
            # display the image for a critical battery
            img = pygame.image.load("assets/images/BatteryWarningCritical.png")
        
        img = pygame.transform.scale(img, (50, 50))
        # place the image below the battery bar
        self.screen.blit(img, (45, 410))