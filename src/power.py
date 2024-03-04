'''
klasse fuer die anzeige des balkens mit der aktuellen leistung in kW
'''

import pygame
from src.data import Data

class Power:
    def __init__(self, screen):
        self.screen = screen
        # die leistung aus der data klasse holen
        self.power = Data().power

    def update(self):
        self.powerBar(self.power)

    # funktion fuer den power balken
    # power . . . aktuelle leistung in kW 0-10
    def powerBar(self, power):
        color = (200, 200, 0) # gelb
        # glow blitten
        image = pygame.image.load("./assets/images/BatteryGlowYellow.png")
        self.screen.blit(image, (691, 60))

        # den hintergrund des power balkens zeichnen
        pygame.draw.rect(self.screen, (50, 50, 50), (710, 80, 40, 320))
        pygame.draw.rect(self.screen, color, (710, 400 - power * 3.2, 40, power * 3.2))

        # die aktuelle leistung in kW anzeigen
        font1 = pygame.font.Font('assets/fonts/Seven_Segment.ttf', 30)
        text1 = font1.render(str(power/10), False, (255, 255, 255))
        font2 = pygame.font.SysFont('Arial', 26)
        text2 = font2.render("kW", False, (255, 255, 255))
        textRect1 = text1.get_rect().center = (700, 415)
        textRect2 = text2.get_rect().center = (740, 415)
        self.screen.blit(text1, textRect1)
        self.screen.blit(text2, textRect2)