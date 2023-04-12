import itertools


values = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "T",
    "J",
    "Q",
    "K",
    "A",
]

suits = [
    "S",
    "H",
    "D",
    "C",
]

cards = list(itertools.product(values, suits))
