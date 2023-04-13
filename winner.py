from typing import List, Tuple

from deck import sort_values, values
from harmony import RoyalFlush, StraightFlush, FourOfAKind, FullHouse, Flush, Straight, ThreeOfAKind, TwoPairs, OnePair, \
    HighCard, HarmonyMode


class PlayerCards:
    def __init__(self, card_1, card_2):
        self.cards = (card_1, card_2)

    def __str__(self):
        return f"{self.cards}"


class CommunityCards:
    def __init__(self, *cards):
        self.cards = cards

    def __str__(self):
        return f"{self.cards}"


def winner(community_cards: CommunityCards, players: List[PlayerCards]) -> List[Tuple[PlayerCards, HarmonyMode]]:
    combs = []

    for p in players:
        combs.append(
            (p, list(sort_values((*community_cards.cards, *p.cards)))),
        )

    for harmony_cls in (RoyalFlush, StraightFlush, FourOfAKind, FullHouse, Flush, Straight,
                        ThreeOfAKind, TwoPairs, OnePair, HighCard):

        applied_players = []

        for p in combs:
            player = p[0]
            cards = p[1]

            hrm = harmony_cls(cards)
            if hrm.applies():
                applied_players.append(
                    (player, hrm)
                )

        if len(applied_players) == 0:
            continue
        elif len(applied_players) == 1:
            return applied_players[0]
        else:
            kickers = list(map(lambda applied: applied[1].primary + applied[1].kicker, applied_players))

            winners = kicker_resolution(kickers)

            return [applied_players[i] for i in winners]


def kicker_resolution(all_kickers: List[List[str]]) -> List[int]:
    kk = []
    for kickers in all_kickers:
        kk.append(
            list(map(lambda k: values.index(k), kickers))
        )

    for i in range(len(kk[0])):
        ith_kickers = list(map(lambda kicks: kicks[i], kk))
        max_ith = max(ith_kickers)
        indices = [i for i, x in enumerate(ith_kickers) if x == max_ith]

        if len(indices) == 1:
            return [indices[0]]
        else:
            for k_idx, k in enumerate(kk):
                if k_idx not in indices:
                    for l in range(len(k)):
                        k[l] = 0

    results = []
    for idx, k in enumerate(kk):
        if all(k):
            results.append(idx)

    return results


def main():
    p1 = PlayerCards(("4", "S"), ("6", "C"))
    p2 = PlayerCards(("4", "D"), ("K", "H"))

    com = CommunityCards(("4", "D"), ("J", "H"), ("A", "S"), ("T", "S"), ("2", "C"))


if __name__ == '__main__':
    main()
