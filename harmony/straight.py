from deck import straight
from harmony import HarmonyMode


class Straight(HarmonyMode):
    def applies(self) -> bool:
        st = straight(self.cards)
        self.primaries = [st]
        return bool(st)
