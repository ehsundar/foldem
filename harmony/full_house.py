from deck import mappings
from harmony import HarmonyMode


class FullHouse(HarmonyMode):
    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)
        cardinalities = map(lambda val_list: len(val_list), value_map.values())
        if 3 in cardinalities and 2 in cardinalities:
            return True

        return False

    def __str__(self):
        return f"full house"
