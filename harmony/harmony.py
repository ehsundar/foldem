from typing import Collection, List


class HarmonyMode:
    def __init__(self, cards: Collection):
        assert len(cards) == 7
        self.cards = cards
        self._primary = []
        self._kicker = []

    def applies(self) -> bool:
        return False

    @property
    def primaries(self) -> List[str]:
        return self._primary

    @primaries.setter
    def primaries(self, value):
        assert len(value) <= 5
        self._primary = value

    @property
    def kickers(self):
        return self._kicker

    @kickers.setter
    def kickers(self, value):
        assert len(value) <= 5
        self._kicker = value

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        if self.primaries:
            if self.kickers:
                return f"{self.name} ({self.primaries}) kick: ({self.kickers})"
            else:
                return f"{self.name} ({self.primaries})"
        else:
            return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        return (self._primary + self._kicker)[item]

    def __len__(self):
        return len(self._primary) + len(self._kicker)
