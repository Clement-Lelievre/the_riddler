"""https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/
Both parts are very interesting to me"""

# part 2 (classic)

"""The goal is to identify as many words that meet the following criteria:

    The word must be at least four letters long.
    The word must include the central letter.
    The word cannot include any letter beyond the seven given letters.

Note that letters can be repeated. For example, the words GAME and AMALGAM are both acceptable words. 
Four-letter words are worth 1 point each, while five-letter words are worth 5 points, 
six-letter words are worth 6 points, seven-letter words are worth 7 points, etc. 
Words that use all of the seven letters in the honeycomb are known as “pangrams” and earn 7 bonus points 
(in addition to the points for the length of the word). So in the above example, MEGAPLEX is worth 15 points.

Which seven-letter honeycomb results in the highest possible game score? 
To be a valid choice of seven letters, no letter can be repeated, it must not contain the letter S 
(that would be too easy) and there must be at least one pangram.

For consistency, please use this word list (word_list.txt) to check your game score."""

from tqdm import tqdm

# filtering on the most common letters in English language might help fasten the algo


def get_valid_honeycombs() -> tuple:
    with open("word_list.txt", "r") as f:
        word_list = [
            word.lower().strip()
            for word in f.read().splitlines()
            if len(word) >= 4 and "s" not in word
        ]
    pangram_words = [w for w in word_list if len(set(w)) == 7]
    valid_honeycombs = set("".join(sorted(set(w))) for w in pangram_words)
    return valid_honeycombs, word_list


def score_honeycomb(honeycomb: str, word_list: list[str]) -> tuple:
    best_score = 0
    honeycomb_set = set(honeycomb)
    best_central = None
    for letter in honeycomb:
        current_score = 0
        central = letter
        for word in word_list:
            if central in word and set(word).issubset(honeycomb_set):
                current_score += 1 if len(word) == 4 else len(word)
                current_score += 7 if len(set(word)) == 7 else 0
        if current_score > best_score:
            best_score = current_score
            best_central = central
    return best_score, best_central


def solve() -> None:
    valid_honeycombs, word_list = get_valid_honeycombs()
    best_score = 0
    best_honeycomb = None
    best_central = None
    for honeycomb in tqdm(valid_honeycombs):
        score, central = score_honeycomb(honeycomb, word_list)
        if score > best_score:
            best_score = score
            best_honeycomb = honeycomb
            best_central = central
            assert best_central in best_honeycomb
            print(f"{best_score=}, {best_honeycomb=}, {best_central=}")


if __name__ == "__main__":
    solve()  # 3898 points, 'aeginrt', central = 'r'

# after solving the problem in a quite naive fashion above, I wondered about ways to optimize the algo
# here is a great approach by Peter Norvig: https://github.com/norvig/pytudes/blob/main/ipynb/SpellingBee.ipynb
