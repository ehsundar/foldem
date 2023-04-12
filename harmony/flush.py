from deck import mappings
from harmony import HarmonyMode


class Flush(HarmonyMode):
    def applies(self) -> bool:
        _, suits_map = mappings(self.cards)
        for suit, values in suits_map.items():
            if len(values) >= 5:
                return True

        return False

    def __str__(self):
        return f"flush"
