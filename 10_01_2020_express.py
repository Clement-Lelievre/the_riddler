"""https://fivethirtyeight.com/features/can-you-find-a-number-worth-its-weight-in-letters/
Here's a quick puzzle about the number 2020. Of all the fractions out there that are greater than 1/2020 but less than 1/2019, 
one has the smallest denominator. Which fraction is it?"""


def solve() -> None:
    denom = 2020
    LOWER = 1 / 2020
    UPPER = 1 / 2019
    found = False
    while not found:
        numerator = 1
        frac = numerator / denom
        while frac < UPPER:
            frac = numerator / denom
            if LOWER < frac < UPPER:
                print(f"{numerator=} {denom=}")
                found = True
                break
            numerator += 1
        denom += 1


if __name__ == "__main__":
    solve()  # 2/4039
