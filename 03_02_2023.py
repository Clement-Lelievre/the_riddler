import random

# 1) old school calcs with pen and paper

# compute the probability of traversing the song without any error
p_verse_success = 99 / 100
nb_verses = 99
p_song_success = (p_verse_success) ** nb_verses  # ~37%

# compute the average number of tries before fully traversing the song without error
nb_flawed_tries_required = 1 / p_song_success

print(
    f"On average, it will take {round(nb_flawed_tries_required, 3)} failed attempts before success"
)
# print(f"{nb_flawed_tries_required=}")
# when making a mistake, on average after what verse does it happen?
# for it to happen after verse k (k between 1 and 99 inclusive), the proba is (99/100)**(k-1) * (1/100)
def avg_nb_verses_when_error():
    """Returns the average number of verses sung when making an error,
    by computing the derivative of the geometric sum"""
    return sum(
        k * (1 / 100) * (p_verse_success) ** (k - 1) for k in range(1, nb_verses + 1)
    )


print(
    f"IF an error happens, on average it does so after {round(avg_nb_verses_when_error(),2)} verses"
)
# compute the answer
pen_paper_answer = (1 / p_song_success) * avg_nb_verses_when_error() + nb_verses
print(f"{pen_paper_answer=}")


# 2) confirmation with a Monte Carlo simulation


def sing_full_song(verse_nb: int = 99, proba_forget_verse: float = 1 / 100) -> int:
    """Simulates the full singing of all verses, i.e. keeps trying to sing each verse from 99 to 1 until success"""
    nb_verses_sung = 0
    while verse_nb:
        verse_nb -= 1  # sing verse number <verse_nb>
        nb_verses_sung += 1
        if random.random() <= proba_forget_verse:  # forget verse
            verse_nb = 99  # go back to start
    return nb_verses_sung


def monte_carlo(n_sim: int = 10_000) -> int:
    return sum(sing_full_song() for _ in range(n_sim)) / n_sim


print(f"Confirmation with Monte Carlo: {monte_carlo()=}")
