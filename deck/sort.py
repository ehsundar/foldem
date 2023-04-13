from functools import cmp_to_key
from typing import Iterable

from .cards import values


def sort_values(crds: Iterable) -> Iterable[str]:
    def cmp(n1, n2):
        val1 = n1
        val2 = n2
        if isinstance(n1, tuple):
            val1 = n1[0]
            val2 = n2[0]

        if values.index(val1) < values.index(val2):
            return -1
        elif values.index(val1) > values.index(val2):
            return 1
        else:
            return 0

    return sorted(crds, key=cmp_to_key(cmp), reverse=True)
