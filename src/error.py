'''
class for the error events
'''

# imports
import pygame

class Error:
    def __init__(self, screen):
        self.screen = screen
    
    def getData(self):
        # get the data from the other files
        pass

    def update(self):
        self.batteryWarning(34)

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
        self.screen.blit(img, (0, 0))