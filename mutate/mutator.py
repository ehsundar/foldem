import itertools
from datetime import datetime
from typing import Collection

from deck import cards
from judge import PlayerCards, winner


class Mutator:
    def __init__(self, n_players: int, community: Collection, player: PlayerCards):
        assert n_players == 1
        self._n_player = n_players
        self._community = community
        self._player = player

    def wins(self) -> int:
        x_count = 5 - len(self._community)
        present_cards = [*self._community, *self._player.cards]

        other_cards = []
        for c in cards:
            if c not in present_cards:
                other_cards.append(c)

        results = {}

        for comb in itertools.combinations(other_cards, x_count):
            complete_community = [
                *self._community,
                *comb
            ]

            result = winner(complete_community, [self._player])
            name = result[0][1].name

            results[name] = results.get(name, 0)
            results[name] += 1

        sum_all = sum(results.values())
        results["all"] = sum_all

        return results


def main():
    start = datetime.now()
    m = Mutator(1, [("3", "C")], PlayerCards(("2", "H"), ("T", "S")))
    res = m.wins()

    print(res)
    print((datetime.now() - start).seconds)


if __name__ == '__main__':
    main()
