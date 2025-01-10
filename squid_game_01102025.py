"""https://thefiddler.substack.com/p/can-you-survive-squid-game-season

In Season 2 of Squid Game, contestants play a game of “Mingle” (spoiler alert!). For each round of this game, the contestants all wait in a common area until a number is called. They must then split up into groups of that number. Any contestants not in a group of the correct number after 30 seconds … well, let’s just say bad things happen to them. For now, we’ll refer to contestants who make it through a round in a group of the correct size as having “survived” the round.

Suppose there are initially N contestants.

In the first round, contestants must form groups of 1. Okay, that's not too hard; everyone survives. In the second round, contestants must form groups of 2. This continues (with groups of k in round k) until the 38th round, when contestants must form groups of 38.

What is the smallest number N such that there is at least one person who survives all 38 rounds?"""

# TL/DR: 454


def solve_bottom_up(final_round: int = 38) -> int:
    nb_players = 2
    while True:
        # print(f"{nb_players=}", end="\n")
        round_nb = 2
        remaining_players = nb_players
        while remaining_players:
            remaining_players -= remaining_players % round_nb
            # print(f"{remaining_players=} after {round_nb=}")
            if round_nb == final_round and remaining_players:
                print(f"Ans: {nb_players=} {round_nb=}")
                return nb_players
            round_nb += 1
        nb_players += 1


def solve_top_down(final_round: int = 38) -> int:
    players = final_round
    for round_nb in range(final_round - 1, 0, -1):
        if players % round_nb:
            players = (players // round_nb + 1) * round_nb
    print(f"Ans: {players}")
    return players


if __name__ == "__main__":
    assert solve_bottom_up(2) == 2
    assert solve_bottom_up(3) == 4
    assert solve_bottom_up(4) == 6
    assert solve_bottom_up(5) == 10
    assert solve_bottom_up(7) == 18
    solve_bottom_up(38)  # 454

    assert solve_top_down(2) == 2
    assert solve_top_down(3) == 4
    assert solve_top_down(4) == 6
    assert solve_top_down(5) == 10
    assert solve_top_down(7) == 18
    solve_top_down(38)  # 454
