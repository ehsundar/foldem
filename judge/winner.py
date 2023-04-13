from typing import List, Tuple

from deck import sort_values
from harmony import RoyalFlush, StraightFlush, FourOfAKind, FullHouse, Flush, Straight, ThreeOfAKind, TwoPairs, \
    OnePair, HighCard, HarmonyMode
from .game import CommunityCards, PlayerCards
from .kicker import kicker_resolution


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
            return applied_players
        else:
            kickers = list(map(lambda applied: applied[1].primaries + applied[1].kickers, applied_players))

            winners = kicker_resolution(kickers)

            return [applied_players[i] for i in winners]
