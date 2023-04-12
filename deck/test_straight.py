from unittest import TestCase

from deck import straight


class Test(TestCase):
    def test_straight_should_find_normal(self):
        cards = (
            ("K", "C"),
            ("7", "S"),
            ("Q", "C"),
            ("4", "H"),
            ("J", "C"),
            ("T", "C"),
            ("9", "C"),
        )

        result = straight(cards)

        self.assertIsNotNone(result, "should find straight")
        self.assertEqual(result, ("K", "C"))

    def test_straight_should_find_low_end(self):
        cards = (
            ("A", "C"),
            ("7", "S"),
            ("Q", "C"),
            ("4", "H"),
            ("J", "C"),
            ("T", "D"),
            ("3", "C"),
            ("3", "H"),
            ("2", "C"),
            ("5", "S"),
        )

        result = straight(cards)

        self.assertIsNotNone(result, "should find straight")
        self.assertEqual(("5", "S"), result)
