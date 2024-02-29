'''
class for the GPIO pins on the Raspberry Pi 
'''

class Data:
    def __init__(self):
        self.percentage = 85
        self.revs = 1500
        self.maxRevs = 5500
        self.velocity = 35
        self.modeButton = 0
        self.temperature = 'n'
        self.power = 50
        self.collision = 0