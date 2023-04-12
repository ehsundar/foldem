from deck import straight, mappings, values
from .harmony import HarmonyMode


class StraightFlush(HarmonyMode):
    def applies(self) -> bool:
        st = straight(self.cards)

        _, suit_map = mappings(self.cards)
        suit_values = suit_map[st[1]]

        for i in range(1, 5):
            if values[values.index(st[0]) - i] not in suit_values:
                return False

        return True

    def highest(self):
        return straight(self.cards)

    def __str__(self):
        return f"straight flush"


class RoyalFlush(StraightFlush):
    def applies(self) -> bool:
        if super().applies():
            return super().highest()[0] == "A"
        return False

    def __str__(self):
        return f"royal flush"
