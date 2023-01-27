from itertools import combinations, starmap
from math import prod


def is_valid(date1: tuple[int, int], date2: tuple[int, int]) -> bool:
    """Returns whether at least one of the two dates contains both the sum and
    the product of the other date

    Args:
        date1 (tuple[int, int])
        date2 (tuple[int, int])

    Returns:
        bool
    """
    s1, s2, p1, p2 = sum(date1), sum(date2), prod(date1), prod(date2)
    return set(date1) == set((s2, p2)) or set(date2) == set((s1, p1))
    # return (sum(date1) in date2 and prod(date1) in date2) or (sum(date2) in date1 and prod(date2) in date1) # this (my initial code)
    # is wrong because for the case 2/2 as the sum = the product, I gave too much leeway to the other date
    # ie the 4 was contained in excactly the m or the d but not both


max_day_in_month = {
    k: 31 if k % 2 else 30 for k in range(1, 13)
}  # adding Feb 30th doesn't change the end result
all_dates = (
    (mm, dd) for mm in range(1, 13) for dd in range(1, max_day_in_month[mm] + 1)
)
print(sum(starmap(is_valid, combinations(all_dates, 2))))
