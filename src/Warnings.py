class Warnings:
    def __init__(self):
        self.batteryWarning: bool = True
        self.batteryPercent: float = 0

        self.update()

    def update(self):
        self.battery(self.batteryPercent)

    def battery(self, percentage):
        if percentage <= 20:
            self.batteryWarning = True
        else:
            self.batteryWarning = False

    def reset(self):
        self.batteryWarning = False
