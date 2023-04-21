from deck import mappings, sort_values
from .harmony import HarmonyMode


class OnePair(HarmonyMode):
    CODENAME = "OP"

    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)

        for value, suits in value_map.items():
            if len(suits) == 2:
                self.primaries = [value]
                break

        if not self.primaries:
            return False

        for c in sort_values(self.cards):
            if c[0] not in self.primaries:
                self.kickers.append(c[0])
                if len(self.kickers) == 3:
                    break

        return True


class TwoPairs(HarmonyMode):
    CODENAME = "TP"

    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)

        pairs = []
        for value, suits in value_map.items():
            if len(suits) == 2:
                pairs.append(value)

        if len(pairs) < 2:
            return False

        self.primaries = list(sort_values(pairs))[:2]
        for c in sort_values(self.cards):
            if c[0] not in self.primaries:
                self.kickers.append(c[0])
                break

        return True
