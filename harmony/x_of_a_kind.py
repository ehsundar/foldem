from deck import mappings
from .harmony import HarmonyMode


class FourOfAKind(HarmonyMode):
    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)
        for value, suits in value_map.items():
            if len(suits) == 4:
                self.primaries = [value]
                return True

        return False


class ThreeOfAKind(HarmonyMode):
    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)
        for value, suits in value_map.items():
            if len(suits) == 3:
                self.primaries = [value]
                return True

        return False
