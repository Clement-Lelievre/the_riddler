
def solve() -> None:
    seen = set([1])
    def is_the_collatz(n: int) -> bool:
        while True:
            if n in seen:
                return False
            if n == 2024:
                return True
            seen.add(n)
            n = (n // 2, 3 * n + 1)[n % 2]
    i = 0
    while not is_the_collatz(i):
        i += 1
    print(f"answer: {i}")

if __name__=='__main__':
    solve()
