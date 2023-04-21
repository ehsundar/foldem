from deck import straight
from harmony import HarmonyMode


class Straight(HarmonyMode):
    CODENAME = "ST"
    def applies(self) -> bool:
        st = straight(self.cards)
        if st:
            self.primaries = [st[0]]
            return True
        return False
