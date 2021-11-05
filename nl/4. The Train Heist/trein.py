import random


class Trein:
    def __init__(self):
        self._position = 10
        self._has_opened = False

    def beweeg(self):
        while True:
            beweeg = random.choice([-1, 1])
            self._position += beweeg
            arrow = ['->', '<-'][int((beweeg + 1) / 2)]
            yield arrow

    def open_force_field(self):
        if self._has_opened:
            print("Er gebeurt niks")
            return
        if self._position:
            print(f"{abs(self._position)} wagons naast Ethic opent het force field")
        else:
            print("Het force field opent en Ethic daalt neer en haalt de node of power uit zijn houder.")
        self._has_opened = True


trein = Trein()
