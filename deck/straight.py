from .sort import sort_values
from .cards import values


def straight(cards):
    if len(cards) < 5:
        return

    cards = list(sort_values(cards))

    i = 1
    cont = 1
    start = cards[0]
    prev = cards[0][0]

    while i in range(len(cards)):
        val = cards[i][0]
        if values.index(prev) - values.index(val) == 0:
            pass
        elif values.index(prev) - values.index(val) == 1:
            cont += 1
            prev = val

            if cont == 5:
                return start

            if cont == 4 and val == "2" and cards[0][0] == "A":
                return start
        else:
            cont = 1
            start = cards[i]
            prev = val

        i += 1
