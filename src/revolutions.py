'''
klasse fuer die anzeige der Umdrehungen des Motors
'''

import pygame
from src.data import Data
from PIL import Image, ImageDraw

class Revolutions:
    def __init__(self, screen):
        self.screen = screen
        # die umdrehungen und maximalen umdrehungen aus der data klasse holen
        self.revs = Data().revs
        self.maxRevs = Data().maxRevs

    def update(self):
        self.revsBackground()
        self.revs = Data().revs

        self.revBar(self.revs)

    # funktion fuer den hintergrund des umdrehungsbalkens
    def revsBackground(self):
        # den glow des umdrehungsbalkens zeichnen
        image = pygame.image.load("./assets/images/RevsGauge.png")
        self.screen.blit(image, (200, 60))
    
    # funktion fuer den umdrehungsbalken
    # revs . . . aktuelle umdrehungen von 0-maxRevs
    def revBar(self, revs):
        # den winkel des balkens berechnen
        angle = self.calc_angle(revs)

        # wenn der winkel nicht 0 ist, den balken zurechtschneiden und zeichnen
        if angle != 0:
            # den balken zurechtschneiden
            cutimg = self.cut_gauge_sector_from_image(angle)

            # den balken in pygame konvertieren 
            mode = cutimg.mode
            size = cutimg.size
            data = cutimg.tobytes()
            img = pygame.image.fromstring(data, size, mode)
            # den balken zeichnen
            rect = img.get_rect()
            rect.center = 400, 260
            self.screen.blit(img, rect)
        else:
            self.screen.blit(pygame.image.load("./assets/images/RevsGaugeOverlay.png"), (200, 60))

    # funktion um von bilder sektoren auszuschneiden
    # angle . . . winkel um den der sektor ausgeschnitten werden soll
    def cut_gauge_sector_from_image(self, angle):
        min_angle = 0

        # das bild laden
        img = Image.open('./assets/images/RevsGaugeOverlay.png')

        # eine maske erstellen um den sektor auszuschneiden
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)

        # den sektor ausschneiden
        draw.pieslice([(0, 0), img.size], min_angle, -angle, fill=255)

        # das bild mit der maske kombinieren
        result = Image.new('RGBA', img.size, (255, 255, 255, 0))
        result.paste(img, mask=mask)
        return result
    
    # funktion um den winkel des balkens zu berechnen um ihn zurecht zu schneiden
    # 0 - voller balken
    # 207 - leerer balken
    # revs . . . aktuelle umdrehungen 
    def calc_angle(self, revs):
        # den winkel des balkens berechnen
        angle = 207 - (207 / self.maxRevs) * revs
        return angle