# You are breaking into a vault that contains ancient Roman treasure. The vault is locked, and can be opened via a modern-day keypad. The keypad contains three numerical inputs, which are (of course) expressed using Roman numerals: “I,” “II,” and “III.”

# It’s a good thing your accomplice was able to steal the numerical key code to the vault. Earlier in the day, they handed you this code on a scroll of paper. Once at the keypad, you remove the scroll from your pocket and unfurl it. It reads: “IIIIIIIIII.” That’s ten vertical marks, without any clear spacing between them.

# With some quick mental arithmetic, you realize the combination to unlock the door could be anywhere from four digits long to 10 digits long. (Or is it IV digits to X digits?) How many distinct combinations are possible? If two combinations use the same numbers but in a different order, they are considered distinct.


def solve(code_len: int = 10):
    ans = 0

    def recurse(code: str):
        nonlocal ans
        if len(code) == code_len:
            ans += 1
            return
        for i in range(min(3, code_len - len(code))):
            recurse(code + "I" * (i + 1))

    recurse("")
    print(ans)
    return ans


# This Week’s Extra Credit
# Having successfully hacked your way through the first keypad, the door opens to reveal a second door with yet another keypad that has six numerical inputs: “I,” “II,” “III,” “IV,” “V,” “VI,” “VII,” and “VIII.”

# You were expecting this, which is why your accomplice had handed you a second scroll of paper. You unfurl this one as well, hoping they remembered to add spaces between the numbers.

# No such luck. This paper reads: “IIIVIIIVIIIVIII.” That’s 15 characters in total. How many distinct combinations are possible for this second door?


def solve_extra(target: str = "IIIVIIIVIIIVIII"):
    ans = 0
    chars = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

    def recurse(code: str):
        nonlocal ans
        if code != target[: len(code)]:
            return
        if code == target:
            ans += 1
            return
        for char in chars:
            if len(code + char) <= len(target):
                recurse(code + char)

    recurse("")
    print(ans)
    return ans


if __name__ == "__main__":
    assert solve(1) == 1
    assert solve(2) == 2
    assert solve(3) == 4
    assert solve(4) == 7
    solve()  # 274

    assert solve_extra("I") == 1
    assert solve_extra("II") == 2
    assert solve_extra("III") == 4
    assert solve_extra("IV") == 2
    assert solve_extra("VIII") == 8
    solve_extra()  # 4000
