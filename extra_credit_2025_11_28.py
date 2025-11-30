"""Given spices numbered 1 to 100, what is the minimal number N of spices needed
so every number from 1 to 100 can be formed as a sum of a subset of the chosen
spices (each used at most once)
Once N found, how many distinct sets of N integers are there that satisfy this condition?
?

See "extra credit" at https://thefiddler.substack.com/p/can-you-take-the-heat
"""
# the sequence of powers of 2 needs 7 spices (1,2,4,8,16,32,64) to cover integers 1 to 100 included => this cannot be beaten
# it is easily verifiable using the algo below, by replacing 7 with lower values: no sequence will be found

# initially I wanted to check with brute-force, until I realized this wouldn't scale at all
# the key observation is that once a spice sequence works up to n ie covers up to spice number n, then I don't have to check until sum(sequence),
# because by construction I can make up any integer between n and n + sum(sequence[:-1])
# so then I needed a way to walk through all the possibilities and I came up with recursion

Spice = int


def solve() -> None:
    nb_sol = 0

    def recurse(seq: list[Spice], nb_spices: int = 100) -> None:
        nonlocal nb_sol
        if len(seq) > 7:
            return
        covered_up_to = sum(seq)
        if covered_up_to >= nb_spices:
            nb_sol += 1
            print(seq)
            return
        for new_int in range(
            seq[-1] + 1, covered_up_to + 2
        ):  # the binary sequence would be going for covered_up_to + 1, but here we look for less "pure" sequences that work too
            recurse([*seq, new_int])

    recurse([1, 2])
    print(nb_sol)


if __name__ == "__main__":
    solve()
