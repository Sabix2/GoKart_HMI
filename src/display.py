'''
class for the Display changes
'''

import pygame
import sys

# local imports
from src.velocity import Velocity
from src.battery import Battery
from src.revolutions import Revolutions
from src.error import Error
from src.power import Power

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.revolutions = Revolutions(self.screen)
        self.battery = Battery(self.screen)
        self.velocity = Velocity(self.screen)
        self.error = Error(self.screen)
        self.power = Power(self.screen)

    def update(self):
        self.velocity.update()
        self.battery.update()
        self.revolutions.update()
        self.error.update()
        self.power.update()