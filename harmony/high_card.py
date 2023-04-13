from deck import sort_values
from harmony import HarmonyMode


class HighCard(HarmonyMode):
    def applies(self) -> bool:
        self.primaries = list(map(lambda c: c[0], sort_values(self.cards)))[:5]
        return True
