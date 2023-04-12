from .sort import sort_values


def mappings(cards):
    cards = sort_values(cards)

    vals = {}
    suits = {}

    for c in cards:
        vals[c[0]] = vals.get(c[0], [])
        vals[c[0]].append(c[1])

    for c in cards:
        suits[c[1]] = suits.get(c[1], [])
        suits[c[1]].append(c[0])

    return vals, suits
