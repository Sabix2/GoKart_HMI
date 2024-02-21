'''
class for the GPIO pins on the Raspberry Pi 
'''

class Data:
    def __init__(self):
        self.percentage = 50
        self.revs = 1500
        self.maxRevs = 5500
        self.velocity = 450
        self.modeButton = 0
        self.temperature = 0
        self.power = 50