from itertools import combinations, starmap


def is_valid(date1: tuple[int, int], date2: tuple[int, int]) -> bool:
    """Returns whether  at least one pf the two dates contain both the sum and product of the other date

    Args:
        date1 (tuple[int, int]): _description_
        date2 (tuple[int, int]): _description_

    Returns:
        bool: _description_
    """
    m1, d1 = date1
    m2, d2 = date2
    s1, p1 = m1 + d1, m1 * d1
    s2, p2 = m2 + d2, m2 * d2
    return (s1 in date2 and p1 in date2) | (s2 in date1 and p2 in date1)


max_day_in_month = {k: 31 if k % 2 else 30 for k in range(1, 13)} # adding Feb 30th doesn't change the end result
all_dates = ((mm, dd) for mm in range(1, 13) for dd in range(1, max_day_in_month[mm] + 1))
print(sum(starmap(is_valid, combinations(all_dates, 2))))
