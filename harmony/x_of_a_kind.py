from deck import mappings
from .harmony import HarmonyMode


class FourOfAKind(HarmonyMode):
    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)
        for value, suits in value_map.items():
            if len(suits) == 4:
                return True

        return False

    def __str__(self):
        return f"four of a kind"


class ThreeOfAKind(HarmonyMode):
    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)
        for value, suits in value_map.items():
            if len(suits) == 3:
                return True

        return False

    def __str__(self):
        return f"three of a kind"
