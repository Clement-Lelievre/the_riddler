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
    return (sum(date1) in date2 and prod(date1) in date2) | (sum(date2) in date1 and prod(date2) in date1)


max_day_in_month = {k: 31 if k % 2 else 30 for k in range(1, 13)}  # adding Feb 30th doesn't change the end result
all_dates = ((mm, dd) for mm in range(1, 13) for dd in range(1, max_day_in_month[mm] + 1))
print(sum(starmap(is_valid, combinations(all_dates, 2))))
