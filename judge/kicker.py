from typing import List

from deck import values


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

    if len(results) == 0:
        return list(range(len(kk)))

    return results
