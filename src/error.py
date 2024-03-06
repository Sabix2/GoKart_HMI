'''
klasse fuer die anzeige der Fehlermeldungen
'''

import pygame
from src.data import Data

class Error:
    def __init__(self, screen):
        self.screen = screen
        # die daten aus der data klasse holen
        self.percentage = Data().percentage
        self.temperature = Data().temperature
        self.collision = Data().collision

    def update(self):
        self.percentage = Data().percentage
        self.temperature = Data().temperature
        self.collision = Data().collision

        self.batteryWarning(self.percentage)
        self.temperatureWarning(self.temperature)
        self.collisionWarning(self.collision)

    # funktion um fehlermeldungen anzuzeigen wenn die batterie normal/niedrig/kritisch ist
    def batteryWarning(self, percentage):
        if percentage > 20:
            # zeigt das Bild fuer eine normale Batterie
            img = pygame.image.load("assets/images/warnings/BatteryWarningStandby.png")
        elif percentage > 10:
            # zeigt das Bild fuer eine niedrige Batterie
            img = pygame.image.load("assets/images/warnings/BatteryWarningLow.png")
        else:
            # zeigt das Bild fuer eine kritische Batterie
            img = pygame.image.load("assets/images/warnings/BatteryWarningCritical.png")

        # platziert das Bild unter dem Batteriebalken
        self.screen.blit(img, (45, 410))

    # funktion um fehlermeldungen anzuzeigen wenn die Temperatur normal/erhoeht/kritisch ist
    def temperatureWarning(self, temperature):
        if temperature == 'c':
            # zeigt das Bild fuer eine kritische Temperatur
            img = pygame.image.load("assets/images/warnings/TemperatureWarningCritical.png")
        elif temperature == 'i':
            # zeigt das Bild fuer eine erhoehte Temperatur
            img = pygame.image.load("assets/images/warnings/TemperatureWarningIncreased.png")
        else:
            # zeigt das Bild fuer eine normale Temperatur
            img = pygame.image.load("assets/images/warnings/TemperatureWarningStandby.png")

        # platziert das Bild unter dem Temperaturbalken
        self.screen.blit(img, (110, 410))

    # funktion um fehlermeldungen anzuzeigen wenn eine Kollision stattgefunden hat
    def collisionWarning(self, collision):
        if collision == 1:
            # zeigt das Bild fuer eine Kollision
            img = pygame.image.load("assets/images/warnings/CollisionWarningOn.png")
            self.screen.blit(img, (175, 410))
        else:
            # zeigt das Bild fuer keine Kollision
            img = pygame.image.load("assets/images/warnings/CollisionWarningStandby.png")
            self.screen.blit(img, (175, 410))