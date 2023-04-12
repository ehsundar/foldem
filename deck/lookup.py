from typing import Iterable


def lookup(cards, value="X", suit="X") -> Iterable:
    if value == "X" and suit == "X":
        flt = lambda c: True
    elif value == "X":
        flt = lambda c: c[1] == suit
    elif suit == "X":
        flt = lambda c: c[0] == value
    else:
        flt = lambda c: c[0] == value and c[1] == suit

    return filter(flt, cards)
