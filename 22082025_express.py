"""https://thefiddler.substack.com/p/how-far-can-you-run-before-sundown"""

loop_times = [10, 30, 35, 45]


def solve(total_run_time: int = 65):
    ans = 0

    def recurse(score, time_, nb_loops):
        nonlocal ans
        for lt in loop_times:
            if time_ + lt <= total_run_time:
                recurse(score + lt / 10, time_ + lt, nb_loops + 1)
            else:
                ans += score / 4 ** (nb_loops + 1)

    recurse(0, 0, 0)
    print(ans)

solve()  # 4.866455078125
