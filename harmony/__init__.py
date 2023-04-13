from typing import Literal

from .harmony import HarmonyMode

from .flush import Flush
from .full_house import FullHouse
from .high_card import HighCard
from .pairs import OnePair, TwoPairs
from .straight import Straight
from .straight_flush import RoyalFlush, StraightFlush
from .x_of_a_kind import FourOfAKind, ThreeOfAKind

HARMONY_NAMES_TYPE = Literal[
    "RoyalFlush", "StraightFlush", "FourOfAKind", "FullHouse", "Flush", "Straight",
    "ThreeOfAKind", "TwoPairs", "OnePair", "HighCard",
]
