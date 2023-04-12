import itertools

from .mappings import mappings


def flush(cards):
    _, suits = mappings(cards)

    for suit, values in suits.items():
        if len(values) >= 5:
            return list(itertools.product(values[:5], (suit,)))
