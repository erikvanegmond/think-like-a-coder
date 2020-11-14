import random
import time


class Bots(dict):

    def __getitem__(self, item):
        time.sleep(1)
        return super().__getitem__(item)

    def check_bot(self, serial_number):
        return Bot(self[serial_number], serial_number)

    def __repr__(self):
        return str(list(self.keys()))

    def __iter__(self):
        serials = list(self.keys())
        random.shuffle(serials)
        for serial in serials:
            yield Bot(self[serial], serial)


class Bot:
    def __init__(self, furnace_number, serial_number):
        self.furnace_number = furnace_number
        self.serial_number = serial_number

    def __repr__(self):
        return f"Bot(furnace_number={self.furnace_number}, serial_number={self.serial_number})"


def generate_bots(number_of_bots):
    ids = list(range(number_of_bots))
    random.shuffle(ids)

    bots = Bots()
    current_bot = ids.pop()
    bots[current_bot] = 0
    leaves = [current_bot]
    while ids:
        random.shuffle(leaves)
        current_bot = leaves.pop()
        for i in range(random.randint(1, 4)):
            if ids:
                new_bot = ids.pop()
                bots[new_bot] = current_bot
                leaves.append(new_bot)
            else:
                break
    return bots


bots = generate_bots(5000)
