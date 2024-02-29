'''
class for the error events
'''

import pygame
from src.data import Data

class Error:
    def __init__(self, screen):
        self.screen = screen
        self.percentage = Data().percentage
        self.temperature = Data().temperature
        self.collision = Data().collision

    def update(self):
        self.batteryWarning(self.percentage)
        self.temperatureWarning(self.temperature)
        self.collisionWarning(self.collision)

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

        # place the image below the battery bar
        self.screen.blit(img, (45, 410))

    def temperatureWarning(self, temperature):
        if temperature == 'c':
            # display the image for a critical temperature
            img = pygame.image.load("assets/images/warnings/TemperatureWarningCritical.png")
        elif temperature == 'i':
            # display the image for a increased temperature
            img = pygame.image.load("assets/images/warnings/TemperatureWarningIncreased.png")
        else:
            # display the image for a normal temperature
            img = pygame.image.load("assets/images/warnings/TemperatureWarningStandby.png")

        # place the image below the battery bar
        self.screen.blit(img, (110, 410))

    def collisionWarning(self, collision):
        if collision == 1:
            # display the image for a collision
            img = pygame.image.load("assets/images/warnings/CollisionWarningOn.png")
            self.screen.blit(img, (175, 410))
        else:
            # display the image for no collision
            img = pygame.image.load("assets/images/warnings/CollisionWarningStandby.png")
            self.screen.blit(img, (175, 410))