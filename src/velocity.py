'''
klasse für die anzeige der Geschwindigkeit
'''

import pygame
from src.data import Data

class Velocity:
    def __init__(self, screen):
        self.screen = screen
        # die geschwindigkeit aus der data klasse holen
        self.velocity = Data().velocity

    def update(self):
        self.speed(self.velocity)

    # funktion für die geschwindigkeit 
    # speed . . . geschwindigkeit des fahrzeugs
    def speed(self, speed):
        # den text in der mitte des bildschirms anzeigen
        font = pygame.font.Font('assets/fonts/Seven_Segment.ttf', 65)
        text = font.render(str(speed), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (400, 240)
        self.screen.blit(text, textRect)

        # den text in der mitte des bildschirms anzeigen
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("km/h", False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (400, 280)
        self.screen.blit(text, textRect)
