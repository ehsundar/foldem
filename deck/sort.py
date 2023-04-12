from functools import cmp_to_key
from typing import Iterable

from .cards import values


def sort_values(crds: Iterable) -> Iterable[str]:
    def cmp(n1, n2):
        if values.index(n1[0]) < values.index(n2[0]):
            return -1
        elif values.index(n1[0]) > values.index(n2[0]):
            return 1
        else:
            return 0

    return sorted(crds, key=cmp_to_key(cmp), reverse=True)
