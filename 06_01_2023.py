# You and a friend are shooting some hoops at your local basketball court when she issues a challenge:
# She will name a number, which we’ll call N. Your goal is to score exactly N points in as many ways as possible
# using only 2-point and 3-point shots. The order of your shots does not matter.

# For example, there are two ways you could score N = 8 points: four 2-pointers or two 3-pointers and one 2-pointer.

# Your apparently sadistic friend chooses 60 for the value of N. You try to negotiate this number down, but to no avail.
# However, she says you are welcome to pick an even larger value of N. Does there exist an integer N greater than 60 such that
# there are fewer ways to score N points than there are ways to score 60 points?


def nb_unique_ways(score: int) -> int:
    """Computes and returns the number of unique 2x + 3y combinations that
    sum up to `score`

    Note: there are most likely ways to optimize this

    Args:
        score (int): the target score N

    Raises:
        TypeError: if `score` if not an int
        ValueError: if `score` is <= 0

    Returns:
        int: the number of combinations, regardless of shots order
    """
    if not isinstance(score, int):
        raise TypeError
    if score <= 0:
        raise ValueError
    nb = 0
    for i in range(score // 2 + 1):
        if (score - 2 * i) % 3 == 0:
            nb += 1
    return nb


sixty = nb_unique_ways(60)
max_N_tested = 1_000
for i in range(61, max_N_tested):
    if nb_unique_ways(i) < sixty:
        print(i)
        break
else:
    print(f"No solution between 61 and {max_N_tested} found")
# found 61
