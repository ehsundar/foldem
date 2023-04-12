from typing import Collection


class HarmonyMode:
    def __init__(self, cards: Collection):
        assert len(cards) == 7
        self.cards = cards

    def applies(self) -> bool:
        return False
