from unittest import TestCase

from cache.access import Cache


class TestCache(TestCase):

    def parse_cards(self, cards: str):
        c = []
        for i in range(len(cards) // 2):
            c.append(
                (cards[2 * i], cards[2 * i + 1])
            )

        return c

    def test_get(self):
        c = Cache("foldem_cache")

        mode = c.get(self.parse_cards("7S4C3H3S2C2D2H"))

        self.assertEqual(["3", "2"], mode.primaries)
        self.assertEqual([], mode.kickers)
