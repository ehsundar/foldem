from unittest import TestCase

from .game import PlayerCards, CommunityCards
from .kicker import kicker_resolution
from .winner import winner


class TestWinner(TestCase):
    def test_kicker_resolution(self):
        results = kicker_resolution(
            [
                ["J", "T", "5"],
                ["J", "T", "3"],
                ["J", "9", "8"],
            ]
        )

        self.assertEqual([0], results)

    def test_kicker_resolution_on_first_kicker(self):
        results = kicker_resolution(
            [
                ["J", "T", "5"],
                ["K", "T", "3"],
                ["J", "9", "8"],
            ]
        )

        self.assertEqual([1], results)

    def test_kicker_resolution_on_tie(self):
        results = kicker_resolution(
            [
                ["J", "T"],
                ["J", "T"],
                ["J", "T"],
            ]
        )

        self.assertEqual([0, 1, 2], results)

    def test_winner_one_pair(self):
        p1 = PlayerCards(("4", "S"), ("T", "C"))
        p2 = PlayerCards(("4", "D"), ("2", "H"))

        com = CommunityCards(("4", "D"), ("J", "H"), ("A", "S"), ("T", "S"), ("2", "C"))

        w = winner(com, [p1, p2])

        self.assertEqual(1, len(w))
        self.assertEqual(p1, w[0][0])
