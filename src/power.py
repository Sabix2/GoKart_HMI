'''
class for the power visualization
'''

import pygame
from src.data import Data

class Power:
    def __init__(self, screen):
        self.screen = screen
        self.power = Data().power

    def update(self):
        self.powerBar(self.power)

    # function to draw a battery bar that gets an input 0-100, the bar should be standing and on the left side
    def powerBar(self, power):
        #yellow as color
        color = (200, 200, 0)
        #blit outer glow
        image = pygame.image.load("./assets/images/BatteryGlowYellow.png")
        self.screen.blit(image, (691, 60))

        # draw the background of the battery bar
        pygame.draw.rect(self.screen, (70, 50, 50), (710, 80, 40, 320))
        # draw the battery bar, which changes with the percentage
        pygame.draw.rect(self.screen, color, (710, 400 - power * 3.2, 40, power * 3.2))

        #draw the text, which inicates the power in kW below the bar
        font1 = pygame.font.Font('assets/fonts/Seven_Segment.ttf', 30)
        text1 = font1.render(str(power/10), False, (255, 255, 255))
        font2 = pygame.font.SysFont('Arial', 26)
        text2 = font2.render("kW", False, (255, 255, 255))
        textRect1 = text1.get_rect().center = (700, 415)
        textRect2 = text2.get_rect().center = (740, 413)
        self.screen.blit(text1, textRect1)
        self.screen.blit(text2, textRect2)