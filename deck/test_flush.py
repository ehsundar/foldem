from unittest import TestCase

from deck import flush


class Test(TestCase):
    def test_flush_should_find_normal(self):
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

        result = flush(cards)

        self.assertIsNotNone(result, "should find flush")
        self.assertEqual(("A", "C"), result[0])
