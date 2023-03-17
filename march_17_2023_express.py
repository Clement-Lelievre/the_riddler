"""My take on 03/01/2023 riddler express"""
import logging
from collections import deque

logging.basicConfig(level=logging.INFO)

# bruteforcing all possible combinations is not feasible given the search space
# I'll try starting from '1', and exploring the states from there, adding neighbouring states to the queue
# there is no need for A* or priority queue or anything like that, as all that matters is to cover all valid combinations,
# in whatever order

# I'll be tracking two things: the combination itself, using an ordered and mutable data structure (list of ints),
# and the notes reverted to so far, in an unordered and mutable array (set of ints)


def find_nb_combinations(verbose: bool = False) -> list[list[int]]:
    """They must always play the next note (i.e., adding 1 to the previous note), unless they revert to a previous note.
    At no point can they play the same note twice in a row.
    Notes 1 and 8 — that is, the first and last notes — can be played only once.
    They can only revert to a given note at most once.
    Once they have reverted to a specific note, they cannot then revert to an earlier note in the sequence"""
    queue: deque = deque([([1], set())])
    valid_combs = []
    # given the low number of valid combinations I can afford to store them in memory, instead of couting them
    while queue:
        comb, reverted_to = queue.pop()
        # stopping criterion
        if comb[-1] == 8:
            valid_combs.append(comb)
            continue
        # add next note
        queue.append((comb + [comb[-1] + 1], reverted_to))
        # revert to every legal note, if possible
        revertible_notes = [
            note
            for note in set(comb) - reverted_to
            if note not in {1, comb[-1], comb[-1]+1}
            and comb.index(note) > max(map(comb.index, reverted_to), default=0)
        ]
        queue.extend(
            (comb + [revertible_note], reverted_to | {revertible_note})
            for revertible_note in revertible_notes
        )
    if verbose:
        logging.info(f"Answer: {len(valid_combs)}")
    return valid_combs


if __name__ == "__main__":
    find_nb_combinations(verbose=True)
