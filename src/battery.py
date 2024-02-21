'''
class for the battery visualization
'''

import pygame
from src.data import Data

class Battery:
    def __init__(self, screen):
        self.screen = screen
        self.percentage = Data().percentage

    def update(self):
        self.batteryBar(self.percentage)

    # function to draw a battery bar that gets an input 0-100, the bar should be standing and on the left side
    def batteryBar(self, percentage):
        if percentage > 20:
            #green as color
            color = (0, 200, 0)
            #blit outer glow
            image = pygame.image.load("./assets/images/BatteryGlowGreen.png")
            self.screen.blit(image, (31, 60))
        elif percentage > 10:
            #yellow as color
            color = (200, 200, 0)
            #blit outer glow
            image = pygame.image.load("./assets/images/BatteryGlowYellow.png")
            self.screen.blit(image, (31, 60))
        else:
            #red as color
            color = (200, 0, 0)
            #blit outer glow
            image = pygame.image.load("./assets/images/BatteryGlowRed.png")
            self.screen.blit(image, (31, 60))

        # draw the background of the battery bar
        pygame.draw.rect(self.screen, (50, 50, 50), (50, 80, 40, 320))
        # draw the battery bar, which changes with the percentage
        pygame.draw.rect(self.screen, color, (50, 400 - percentage * 3.2, 40, percentage * 3.2))