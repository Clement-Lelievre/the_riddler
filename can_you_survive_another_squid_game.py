"""https://thefiddler.substack.com/p/can-you-survive-another-squid-game"""

# base challenge
import random
from collections import defaultdict


def solve_base() -> None:
    contestants = list(range(1, 20))
    ind_to_eliminate = 1  # index
    while (lc := len(contestants)) > 1:
        contestants.pop(ind_to_eliminate)
        lc -= 1
        ind_to_eliminate = (ind_to_eliminate + 1) % lc
    print(contestants[0])


# extra credit


def solve_extra(n_sim: int = 5_000_000) -> None:
    """Solves the extra credit with a Monte Carlo simulation

    Args:
        n_sim (int, optional): number of games to play. Defaults to 5_000_000.
    """
    results: dict = defaultdict(int)

    def one_sim() -> None:
        contestants = list(range(1, 20))
        ind_to_eliminate = 1  # index
        while (lc := len(contestants)) > 1:
            contestants.pop(ind_to_eliminate)
            lc -= 1
            ind_to_eliminate = (ind_to_eliminate + random.choice((1, 2))) % lc
        results[contestants[0]] += 1

    [one_sim() for _ in range(n_sim)]  # unassigned but used coz may be faster than for loop
    print(
        f"Top 3 most likely (number, nb games won): {sorted(results.items(), key=lambda data: -data[1])[:3]} out of {n_sim} games"
    )


if __name__ == "__main__":
    solve_base()
    solve_extra()
