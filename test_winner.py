from unittest import TestCase

from winner import kicker_resolution


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
