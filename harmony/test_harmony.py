from unittest import TestCase

from harmony import OnePair


class TestHarmonyMode(TestCase):
    def test_serialize(self):
        hrm = OnePair(
            [
                ("A","S"),
                ("K", "C"),
                ("2", "H"),
                ("7", "S"),
                ("6", "D"),
                ("3", "C"),
                ("3", "H"),
            ]
        )

        hrm.applies()

        self.assertEqual("ASKC7S6D3C3H2H-OP/3/AK7/      ", hrm.serialize())

    def test_deserialize(self):
        hrm = OnePair.deserialize("ASKC7S6D3C3H2H-OP/3/AK7/      ")

        self.assertEqual(("K", "C"), hrm.cards[1])
        self.assertEqual(["3"], hrm.primaries)
        self.assertEqual(["A", "K", "7"], hrm.kickers)

