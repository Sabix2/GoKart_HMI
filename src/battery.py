'''
klasse für die anzeige des Batterie Status
'''

import pygame
from src.data import Data

class Battery:
    def __init__(self, screen):
        self.screen = screen
        # den batterie status aus der data klasse holen
        self.percentage = Data().percentage

    def update(self):
        self.batteryBar(self.percentage)

    # funktion für den batterie balken
    # 100-21% = grün
    # 20-11% = gelb
    # 10-0% = rot
    # percentage . . . prozentsatz der batterie 0-100
    def batteryBar(self, percentage):
        if percentage > 20:
            color = (0, 200, 0) # grün
            # äußeren glow blitten
            image = pygame.image.load("./assets/images/BatteryGlowGreen.png")
            self.screen.blit(image, (31, 60))
        elif percentage > 10:
            color = (200, 200, 0) # gelb
            # äußeren glow blitten
            image = pygame.image.load("./assets/images/BatteryGlowYellow.png")
            self.screen.blit(image, (31, 60))
        else:
            color = (200, 0, 0) # rot
            # äußeren glow blitten
            image = pygame.image.load("./assets/images/BatteryGlowRed.png")
            self.screen.blit(image, (31, 60))

        # den hintergrund des batterie balkens zeichnen
        pygame.draw.rect(self.screen, (50, 50, 50), (50, 80, 40, 320))
        # den batterie balken zeichnen, welcher sich mit dem prozentsatz ändert
        pygame.draw.rect(self.screen, color, (50, 400 - percentage * 3.2, 40, percentage * 3.2))