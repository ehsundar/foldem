from deck import straight
from harmony import HarmonyMode


class Straight(HarmonyMode):
    def applies(self) -> bool:
        st = straight(self.cards)
        return bool(st)

    def __str__(self):
        return f"straight"
