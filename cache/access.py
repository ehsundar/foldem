import itertools
from os import path

from deck import cards, values
from harmony import HarmonyMode, FullHouse


class Cache:
    def __init__(self, directory: str):
        self._dir = directory

    def get(self, current_cards) -> HarmonyMode:
        filename = f"{current_cards[0][0]}{current_cards[0][1]}-{current_cards[1][0]}{current_cards[1][1]}.dat"

        with open(path.join(self._dir, filename), "r") as f:
            pos = self._get_row_number(current_cards)
            f.seek(pos * 31)

            row = f.read(30)
            codename = HarmonyMode.extract_codename(row)

            match codename:
                case "FH":
                    return FullHouse.deserialize(row)

    def _get_row_number(self, current_cards) -> int:
        idx = 52 - cards.index(current_cards[1])
        file_cards = list(reversed(cards))[idx:]
        file_cards_len = len(file_cards)

        # first_comb = next(itertools.combinations(file_cards, 5))
        #
        # row_idx = 0
        # for i in range(5):
        #
        #     row_idx += abs(file_cards.index(first_comb[4-i]) - file_cards.index(current_cards[6-i]))* (file_cards_len**i)
        #
        # return row_idx

        counter = 0
        current_5_cards = tuple(current_cards[2:])
        for card_set in itertools.combinations(file_cards, 5):
            if card_set == current_5_cards:
                return counter
            counter += 1
