import random
import time


class Bots(dict):

    def __getitem__(self, item):
        time.sleep(1)
        return super().__getitem__(item)

    def check_bot(self, serie_nummer):
        return Bot(self[serie_nummer], serie_nummer)

    def __repr__(self):
        return str(list(self.keys()))

    def __iter__(self):
        serials = list(self.keys())
        random.shuffle(serials)
        for serie in serials:
            yield Bot(self[serie], serie)


class Bot:
    def __init__(self, fornuis_nummer, serie_nummer):
        self.fornuis_nummer = fornuis_nummer
        self.serie_nummer = serie_nummer

    def __repr__(self):
        return f"Bot(fornuis_nummer={self.fornuis_numner}, serie_nummer={self.serie_nummer})"


def generate_bots(aantal_bots):
    ids = list(range(aantal_bots))
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
