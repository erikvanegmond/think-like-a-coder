import random


class Slot:
    def __init__(self):
        self._key = random.randint(1, 100)
        self._position = 1

    def bekijk_kleur(self):
        return "groen" if self._key == self._position else "rood"

    def bekijk_stand(self):
        return self._position

    def draai_schijf(self, aantal_posities: int) -> None:
        """
        Draai de schijf van het slot met het aantal posities met de klok mee zoals aangegeven in `aantal_posities`.
        :param aantal_posities:
        """
        self._position = (self._position + aantal_posities) % 100
        self._position = self._position if self._position else 100

    def __repr__(self):
        return f"kleur: {self.bekijk_kleur()}, positie: {self.bekijk_stand()}"

    def open(self):
        if self._key == self._position:
            print("Het slot opent.")
        else:
            print("Het slot blijft dicht.")
