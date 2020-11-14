import random


class Lock:
    def __init__(self):
        self._key = random.randint(1, 100)
        self._position = 1

    def check_color(self):
        return "green" if self._key == self._position else "red"

    def check_dial(self):
        return self._position

    def spin_dial(self, amount):
        self._position = (self._position + amount) % 100
        self._position = self._position if self._position else 100

    def __repr__(self):
        return f"color: {self.check_color()}, position: {self.check_dial()}"

    def open(self):
        if self._key == self._position:
            print("The lock opens.")
        else:
            print("The lock stays closed.")
