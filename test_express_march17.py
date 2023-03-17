"Test suite for my solution to the March 17, 2023 Express challenge"
import pytest

from march_17_2023_express import find_nb_combinations

SAMPLE_VALID_PROVIDED = [
    "12345678",
    "1234567-234567-34567-4567-567-678",
    "1234-234567-678",
    "1234567-345-4567-5678",
    "123-234567-3456-45678",
    "1234563678",
]
SAMPLE_INVALID_PROVIDED = [
    "1245678",
    "12437568",
    "12345-34678",
    "1234-3456-345678",
    "12345-456-2345678",
    "12345-567-678",
    "123-1234567-5678",
    "1234-23456-5678-78",
]


@pytest.fixture
def valid_combs():
    return find_nb_combinations()


def test_no_duplicates(valid_combs):
    assert len(valid_combs) == len(set(map(tuple, valid_combs)))


def test_both_end_values(valid_combs):
    assert all(comb[0] == 1 and comb[-1] == 8 for comb in valid_combs)


def test_no_double_one_eight(valid_combs):
    """Checks that each valid combination contains exactly one 1 and one 8"""
    assert (comb.count(1) == comb.count(8) == 1 for comb in valid_combs)


def test_max_len(valid_combs):
    assert max(map(len, valid_combs)) == len("1234567234567345674567567678")


def test_min_len(valid_combs):
    assert min(map(len, valid_combs)) == len("12345678")


@pytest.mark.parametrize(
    "comb",
    [list(map(int, elem.replace("-", ""))) for elem in SAMPLE_VALID_PROVIDED],
    ids=SAMPLE_VALID_PROVIDED,
)
def test_presence(comb, valid_combs):
    assert comb in valid_combs


@pytest.mark.parametrize(
    "comb",
    [list(map(int, elem.replace("-", ""))) for elem in SAMPLE_INVALID_PROVIDED],
    ids=SAMPLE_INVALID_PROVIDED,
)
def test_absence(comb, valid_combs):
    assert comb not in valid_combs


def test_next_value(valid_combs):
    for comb in valid_combs:
        for i in range(1, len(comb)):
            assert (comb[i] in comb[: i - 1]) or (comb[i] == comb[i - 1] + 1)


def test_no_twice_same_value(valid_combs):
    for comb in valid_combs:
        for i in range(1, len(comb)):
            assert comb[i] != comb[i - 1]


def test_revert_at_most_once(valid_combs):
    for comb in valid_combs:
        reverted_to = []
        for i in range(1, len(comb)):
            if comb[i] != comb[i - 1] + 1:
                reverted_to.append(comb[i])
        assert len(reverted_to) == len(set(reverted_to))


# TO DO: Once they have reverted to a specific note, they cannot then revert to an earlier note in the sequence
