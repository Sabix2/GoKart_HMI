'''
sorgt dafür, dass das der Bidlschirm angezeigt wird und am laufen bleibt
'''

import pygame
from src.display import Display

#pygame initialisieren
pygame.init()

# erstelle das Fenster
screen = pygame.display.set_mode((800, 480), pygame.NOFRAME)

# instanziiere das Display
Frame = Display(screen)

# schleife für das Fenster erstellen 
running = True
while running:
    # erstelle den hintergrund
    screen.fill((40, 40, 40))

    # schleife für die events
    Frame.update()

    # den Bildschirm aktualisieren
    pygame.display.flip()
