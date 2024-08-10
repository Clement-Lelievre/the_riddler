"""https://thefiddler.substack.com/p/can-you-hack-the-olympics

In the 2002 Winter Olympics, figure skaters first completed a “short program,” for which they received a set of numerical scores (out of 6.0). 
Based on these numerical scores, skaters were ranked from 1 (first) to N (last), where N was the total number of skaters. The next day, skaters similarly completed a longer, 
“free skate” that received numerical and ordinal scores in the same way.

If a skater's short program ranking was S and their free skate ranking was F, they received an overall score of S/2 + F, which was used for the final ranking of the competitors.
Lower scores were better, and the lowest score earned a gold medal. In the event two or more skaters had the same overall score, whoever had a lower value of F 
(i.e., a better ranking in the free skate) received the better overall ranking.

...

Suppose there are four figure skaters, all of equal merit. In other words, each has an equal chance of ranking anywhere from first to fourth for both the short program 
and the free skate. Each skater's free skate result is independent of their short program result. To keep things (relatively) simple, assume the order in which the skaters 
perform is the same for both the short program and the free skate.

What is the probability that the ultimate gold medalist was not in first place at some point after her free skate (among skaters who completed their free skate)?"""
# quick script for fun during holidays :p

from itertools import permutations

# let players be named a,b,c,d and order of skates be a then b thenc then d for both free and short


def gen_rankings():
    """generate rankings

    Yields:
        _type_: _description_
    """
    for comb_short in permutations("abcd", 4):
        for comb_free in permutations("abcd", 4):
            yield "".join(comb_short) + "".join(comb_free)


# assume order is always: a,b,c,d
# compute final rankings
# identify winner
# identify winner's order at free skate
# check whether winner was winner from perf till last player
# assign the following scores to create intermediate rankings in free skate: 1,2,3,4


def get_rankings(comb: str, after_round: int) -> dict[str, int]:
    """get intermediate or final rankings based on a string representing rankings at short then free skates

    after_round means after which round (1 to 4 inclusive) of free skate"""
    assert after_round in range(1, 5)
    assert len(comb) == 8

    interm_rankings = "".join(
        player for player in comb[4:] if player in "abcd"[:after_round]
    )

    rankings = {
        player: (comb[:4].index(player) + 1) / 2 + interm_rankings.index(player) + 1
        for player in "abcd"[:after_round]
    }
    assert len(rankings) == after_round
    return rankings


# test final rankings
assert get_rankings("abcdabcd", 4)["a"] == 1.5
assert get_rankings("abcdabcd", 4)["d"] == 6
assert get_rankings("cdabbdca", 4)["a"] == 5.5  # the example given in the text
assert get_rankings("cdabbdca", 4)["b"] == 3  # the example given in the text
assert get_rankings("cdabbdca", 4)["c"] == 3.5  # the example given in the text
assert get_rankings("cdabbdca", 4)["d"] == 3  # the example given in the text

# test intermediate rankings
assert set(get_rankings("cdabbdca", 1)) == {"a"}
assert set(get_rankings("cdabbdca", 2)) == {"a", "b"}
assert set(get_rankings("cdabbdca", 3)) == {"a", "b", "c"}
assert set(get_rankings("cdabbdca", 4)) == {"a", "b", "c", "d"}
assert get_rankings("abcdabcd", after_round=1) == {"a": 1.5}
assert get_rankings("abcdabcd", after_round=2) == {"a": 1.5, "b": 3}
assert get_rankings("abcdabcd", after_round=3) == {"a": 1.5, "b": 3, "c": 4.5}
assert get_rankings("abcdabcd", after_round=4) == {"a": 1.5, "b": 3, "c": 4.5, "d": 6}
assert get_rankings("dacbdacb", after_round=2) == {"a": 2, "b": 4}
assert get_rankings("dcbaacdb", after_round=3) == {"a": 3, "b": 4.5, "c": 3}


def get_winner(rankings: dict, comb: str) -> str:
    assert isinstance(rankings, dict)
    # assert all(isinstance(val, float) for val in rankings.values())
    if len(set(rankings.values())) == len(rankings):
        return min(rankings, key=rankings.get)
    # there is a tie
    ties = [k for k, v in rankings.items() if v == min(rankings.values())]
    return min(ties, key=comb[4:].index)


assert get_winner({"a": 3, "b": 4.5, "c": 2}, comb="dummy") == "c"
assert get_winner({"a": 3, "b": 4.5, "c": 3}, comb="abcdcdab") == "c"


def winner_wasnt_always_first(comb: str) -> bool:
    final_rankings = get_rankings(comb, after_round=4)
    winner = get_winner(final_rankings, comb=comb)
    winner_order_passage = "abcd".index(winner) + 1
    if winner_order_passage == 4:
        return False
    for i in range(
        max(2, winner_order_passage), 5
    ):  # no need to compute case where he goes first
        interm_rankings = get_rankings(comb, after_round=i)
        assert len(interm_rankings) == i
        assert (
            winner in interm_rankings
        ), f"{comb=} does not have {winner=} in {interm_rankings=} after round {i} ({winner_order_passage=})"
        interm_winner = get_winner(interm_rankings, comb=comb)
        if interm_winner != winner:
            return True
    return False


assert winner_wasnt_always_first("cdabbdca") is True  # the example given in the text


def solve() -> None:
    total_nb_combs = len(list(gen_rankings()))
    nb_cases = sum(winner_wasnt_always_first(comb) for comb in gen_rankings())
    answer = nb_cases / total_nb_combs
    print(f"{answer=}")


if __name__ == "__main__":
    solve()
