from typing import List

from deck import cards, mappings
from .harmony import HarmonyMode


class OnePair(HarmonyMode):
    def applies(self) -> bool:
        return len(set(map(lambda c: c[0], self.cards))) != len(list(map(lambda c: c[0], self.cards)))

    def pair(self) -> str:
        ns = set()
        for c in self.cards:
            if c[0] in ns:
                return c[0]
            ns.add(c[0])

    def kickers(self) -> List[str]:
        pair = self.pair()
        nums = cards.sort_numbers(self.cards)
        return list(filter(lambda n: n != pair, nums))[:3]

    def __eq__(self, other):
        if self.pair() != other.pair():
            return False

        for i in range(3):
            if self.kickers()[i] != other.kickers()[i]:
                return False

        return True

    def __lt__(self, other):
        if self.pair() != other.pair():
            return cards.values.index(self.pair()) < cards.values.index(other.pair())

        for i in range(3):
            if self.kickers()[i] != other.kickers()[i]:
                return cards.values.index(self.kickers()[i]) < cards.values.index(other.kickers()[i])

    def __str__(self):
        return f"one pair of ({self.pair()})s kickers {self.kickers()}"


class TwoPairs(HarmonyMode):
    def applies(self) -> bool:
        value_map, _ = mappings(self.cards)

        pairs = []
        for value, suits in value_map.items():
            if len(suits) == 2:
                pairs.append(value)

        return len(pairs) >= 2

    def __str__(self):
        return f"two pairs"
