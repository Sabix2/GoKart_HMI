'''
fuehrt alle elemente aus 
'''

from src.velocity import Velocity
from src.battery import Battery
from src.revolutions import Revolutions
from src.error import Error
from src.power import Power
from src.mode import Mode

class Display:
    def __init__(self, screen):
        self.screen = screen

        # instanziiere die einzelnen Elemente
        self.revolutions = Revolutions(self.screen)
        self.battery = Battery(self.screen)
        self.velocity = Velocity(self.screen)
        self.error = Error(self.screen)
        self.power = Power(self.screen)
        self.mode = Mode(self.screen)

    def update(self):
        # fuehre die update funktionen der einzelnen Elemente aus
        self.velocity.update()
        self.battery.update()
        self.revolutions.update()
        self.error.update()
        self.power.update()
        self.mode.update()