from typing import Collection, List

from deck import sort_values


class HarmonyMode:
    CODENAME: str = ""

    def __init__(self, cards: Collection):
        assert len(cards) == 7
        self.cards = sort_values(cards)
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

    def serialize(self) -> str:
        result = "".join(map(lambda c: c[0] + c[1], self.cards))
        result += f"-{self.CODENAME}/"

        if self.primaries:
            result += "".join(self.primaries)

        result += "/"

        if self.kickers:
            result += "".join(self.kickers)

        result += "/"

        assert len(result) <= 30

        return result.ljust(30, " ")

    @classmethod
    def deserialize(cls, serialized_harmony: str):
        cards = []

        for i in range(7):
            cards.append((
                serialized_harmony[2 * i],
                serialized_harmony[2 * i + 1],
            ))

        inst = cls(cards)
        assert inst.CODENAME == inst.extract_codename(serialized_harmony)

        parts = serialized_harmony[18:].strip().split("/")

        assert len(parts) == 3

        inst.primaries = list(parts[0])
        inst.kickers = list(parts[1])

        return inst

    @staticmethod
    def extract_codename(serialized_harmony) -> str:
        return serialized_harmony[15:17]

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
