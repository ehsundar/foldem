from deck import straight, mappings, values
from .harmony import HarmonyMode


class StraightFlush(HarmonyMode):
    CODENAME = "SF"
    def applies(self) -> bool:
        st = straight(self.cards)
        if not st:
            return False

        _, suit_map = mappings(self.cards)
        suit_values = suit_map[st[1]]

        for i in range(1, 5):
            if values[values.index(st[0]) - i] not in suit_values:
                return False

        self.primaries = [st[0]]
        return True


class RoyalFlush(StraightFlush):
    CODENAME = "RF"

    def applies(self) -> bool:
        if super().applies():
            return self.primaries[0] == "A"
        return False
