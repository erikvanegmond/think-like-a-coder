from collections import Counter
from itertools import groupby
import random
import names


class Persoon:
    def __init__(self, kleur_ogen, kleur_haar, bril, naam):
        self.kleur_ogen = kleur_ogen
        self.kleur_haar = kleur_haar
        self.naam = naam
        self.bril = bril

    def aantal_klinkers(self):
        counted = Counter(self.naam.lower())
        return sum(counted[v] for v in "aeiouy")

    def ten_minste_een_opeenvolgende(self):
        return max(len(list(v)) for _, v in groupby(self.naam.lower())) > 1

    def check_haar(self):
        return self.kleur_haar

    def check_ogen(self):
        return self.kleur_ogen

    def check_bril(self):
        return self.bril

    def vraag_naam(self):
        return self.naam

    def __repr__(self):
        return f"Persoon(kleur_ogen={self.kleur_ogen}, kleur_haar={self.kleur_haar}, bril={self.bril}, naam={self.naam})"

def _persoon_check(persoon):
    if persoon.check_ogen() == "groen":
        if persoon.check_haar() == "rood":
            if not persoon.ten_minste_een_opeenvolgende():
                return False
        if persoon.check_bril():
            if persoon.aantal_klinkers() != 2:
                return False
        else:
            if persoon.aantal_klinkers() != 3:
                return False
        return True
    else:
        return False


def _generate_persoon():
    kleur_ogen = random.choices(['bruin', 'blauw', 'hazel', 'amber', 'grijs', 'groen'], weights=[70, 10, 5, 5, 3, 7])[0]
    kleur_haar = random.choices(['bruin', 'blauw', 'zwart', 'rood', 'blond', 'groen'], weights=[50, 10, 20, 5, 8, 7])[0]
    bril = random.random() > .6
    persoon = Persoon(kleur_ogen=kleur_ogen, kleur_haar=kleur_haar, bril=bril, naam=names.get_first_name())
    return persoon


def _generate_crowd(size=1000):
    crowd = [Persoon(kleur_ogen='groen', kleur_haar="zwart", bril=False, naam="Adila")]
    for _ in range(size):
        p = _generate_persoon()
        if not _persoon_check(p):
            crowd.append(p)
    random.shuffle(crowd)
    return crowd


menigte = _generate_crowd()
