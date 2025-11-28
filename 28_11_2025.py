"""The fiddler, Nov 28th 2025
quick, dirty, and lazy code
"""

from itertools import combinations

S = set(range(1, 11))


def can_make(comb) -> bool:
    comb = (
        1,
        2,
        comb[0],
        comb[1],
    )  # I know that 1 and 2 MUST be in the combination, otherwise we can't make... well, 1 or 2
    todo = S - set(comb)
    for int_to_do in todo:
        found = False
        for i in range(1, len(comb) + 1):
            for subcomb in combinations(comb, i):
                if sum(subcomb) == int_to_do:
                    found = True
                    break
            if found:
                break
        else:
            return False  # couldn't find a combi that sums to int_to_do
    print(comb)
    return True


print(sum(can_make(comb) for comb in combinations(range(3, 11), 2)))
