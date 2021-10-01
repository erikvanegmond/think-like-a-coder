import random


class Train:
    def __init__(self):
        self._position = 10
        self._has_opened = False

    def move(self):
        while True:
            move = random.choice([-1, 1])
            self._position += move
            arrow = ['->', '<-'][int((move + 1) / 2)]
            yield arrow

    def open_force_field(self):
        if self._has_opened:
            print("Nothing happens")
            return
        if self._position:
            print(f"{abs(self._position)} cars next to Ethic the force field opens")
        else:
            print("The force field opens and Ethic swoops in and lifts Node of Power to freedom")
        self._has_opened = True


train = Train()
