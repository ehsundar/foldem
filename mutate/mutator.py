import itertools
from datetime import datetime
from typing import Collection

from deck import cards
from judge import PlayerCards, winner


class Mutator:
    def __init__(self, n_players: int, community: Collection, player: PlayerCards):
        self._n_player = n_players
        self._community = community
        self._player = player

    def wins(self):
        present_cards = [*self._community, *self._player.cards]

        other_cards = []
        for c in cards:
            if c not in present_cards:
                other_cards.append(c)

        results = {}
        lost = 0

        for other_community, other_players in self._get_possible_arrangements(other_cards):
            complete_community = [
                *self._community,
                *other_community
            ]

            players = [PlayerCards(*p) for p in other_players]

            result = winner(complete_community, [self._player, *players])
            if result[0][0] == self._player:
                name = result[0][1].name
                results[name] = results.get(name, 0) + 1
            else:
                lost += 1

        results["won"] = sum(results.values())
        results["lost"] = lost

        return results

    def _get_possible_arrangements(self, available_cards):
        to_choose_community = 5 - len(self._community)
        to_choose = 2 * (self._n_player - 1)

        for chosen in itertools.combinations(available_cards, to_choose_community + to_choose):
            for chosen_for_community in itertools.combinations(chosen, to_choose_community):
                remaining_chosen = tuple(set(chosen) - set(chosen_for_community))
                for arrangement in self._get_arrangements_for_players(remaining_chosen):
                    yield chosen_for_community, arrangement

    def _get_arrangements_for_players(self, player_cards):
        if len(player_cards) == 2:
            return [(player_cards,)]

        results = []
        for pair in itertools.combinations(player_cards, 2):
            remaining_cards = tuple(set(player_cards) - set(pair))
            for arrangement in self._get_arrangements_for_players(remaining_cards):
                results.append(
                    (pair, *arrangement),
                )

        return results


def main():
    start = datetime.now()
    m = Mutator(5, [("3", "C"), ("6", "D"), ("9", "S")], PlayerCards(("8", "H"), ("T", "S")))
    res = m.wins()

    print(res)
    print((datetime.now() - start).seconds)


if __name__ == '__main__':
    main()
