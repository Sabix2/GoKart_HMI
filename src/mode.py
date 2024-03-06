'''
klasse fuer die anzeige des Modus
'''

import pygame
from src.data import Data

class Mode:
    def __init__(self, screen):
        self.screen = screen
        # den modus aus der data klasse holen
        self.mode = Data().mode

    def update(self):
        self.mode = Data().mode

        self.currentMode(self.mode)
    
    # funktion fuer den modus
    # 's' = standart nicht relevant
    # 'e' = eco
    # 'd' = drag
    # modus . . . modus des fahrzeugs
    def currentMode(self, mode):
        # fuer jeden modus den passende
        if mode == 's':
            mode = ''
        elif mode == 'e':
            mode = 'Eco'
        elif mode == 'd':
            mode = 'Drag'

        # den text in die untere mitte des bildschirms zeichnen
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(str(mode), False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (400, 400)
        self.screen.blit(text, textRect)