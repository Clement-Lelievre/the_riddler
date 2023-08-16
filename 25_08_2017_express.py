"""https://fivethirtyeight.com/features/work-a-shift-in-the-riddler-gift-shop/"""
from functools import reduce


def proba_first_half_day_k(k: int) -> float:
    return (
        reduce(lambda x, y: x * y, (100 - i for i in range(k - 1)))
        * (k - 1)
        / (100**k)
    )


def solve() -> None:
    ans = sum(k * proba_first_half_day_k(k) for k in range(2, 102))
    print(ans)


if __name__ == "__main__":
    solve()
