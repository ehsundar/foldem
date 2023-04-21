from deck import mappings, sort_values
from harmony import HarmonyMode


class FullHouse(HarmonyMode):
    CODENAME = "FH"

    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)
        value_count = {}

        for value, suits in value_map.items():
            if len(suits) in (2, 3):
                value_count[value] = len(suits)

        if 3 not in value_count.values() or len(value_count) < 2:
            return False

        self.primaries = list(sort_values(value_count.keys()))[:2]
        return True
