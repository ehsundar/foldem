import dataclasses
from typing import Collection, Iterable, List, Type
from unittest import TestCase

from harmony import OnePair, HarmonyMode, TwoPairs
from .game import PlayerCards, CommunityCards
from .winner import winner


class TestWinner(TestCase):
    @dataclasses.dataclass
    class TestData:
        players: Collection[Iterable[str]]
        community: Iterable[str]
        expected_winners: List[int]
        expected_harmony: Type[HarmonyMode]

    def test_winner_one_pair(self):
        cases = (
            TestWinner.TestData(
                [
                    ("4S", "TC"),
                    ("4D", "2H"),
                ],
                (
                    "4D", "JH", "AS", "9S", "7C",
                ),
                [0],
                OnePair,
            ),
        )

        for c in cases:
            self.run_test_data(c)

    def test_winner_two_pairs(self):
        cases = (
            TestWinner.TestData(
                [
                    ("4S", "TC"),
                    ("4D", "2H"),
                ],
                (
                    "4D", "JH", "AS", "TS", "2C",
                ),
                [0],
                TwoPairs,
            ),
        )

        for c in cases:
            self.run_test_data(c)

    def run_test_data(self, data: TestData):
        players = []
        for p in data.players:
            cards = []
            for c in p:
                cards.append((c[0], c[1]))

            players.append(
                PlayerCards(*cards)
            )

        community_cards = []
        for c in data.community:
            community_cards.append((c[0], c[1]))

        w = winner(CommunityCards(*community_cards), players)

        self.assertEqual(len(data.expected_winners), len(w))

        for ww in w:
            self.assertIsInstance(ww[1], data.expected_harmony)

        for expected in data.expected_winners:
            expected_player = players[expected]

            self.assertIn(expected_player, map(lambda ww: ww[0], w))
