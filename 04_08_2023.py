"""https://thefiddler.substack.com/p/how-many-ways-can-you-raise-the-dots"""

# 1 encode the 64 braille characters, from binary (000000 to 111111) to numpy array
# 2 define a function responsible to say whether two characters are translations of each other
# 3 identify the connected components of the graph of incompatible characters
# 4 for each connected component, keep only one character
import numpy as np
from tqdm import tqdm

NB_ROWS = 3
NB_COLS = 2


def int_to_numpy(nb: int, arr_shape: tuple[int] = (NB_ROWS, NB_COLS)) -> np.ndarray:
    """from a base 10 int, convert it to a numpy array of 0 and 1

    Args:
        nb (int):
        arr_shape (tuple[int], optional): _description_. Defaults to (3, 2).

    Returns:
        np.ndarray: the matrix representation of the binary number
    """
    nb_bin = bin(nb)[2:].zfill(6)
    arr = np.zeros(arr_shape, dtype=int)
    for ind, val in enumerate(map(int, nb_bin)):
        col, row = divmod(ind, NB_ROWS)
        arr[row, col] = val
    # print(f"{nb} is {nb_bin} in binary and \n{arr}\nas a matrix")
    return arr


def is_translation(arr1: np.ndarray, arr2: np.ndarray) -> bool:
    def is_translatable(arr: np.ndarray) -> bool:
        """If and only if at least one edge is full of zeroes"""
        return any(
            (
                arr[0].sum() == 0,
                arr[-1].sum() == 0,
                arr[:, 0].sum() == 0,
                arr[:, -1].sum() == 0,
            )
        )  # for other matrix shapes this needs to be adapted

    if (
        arr1.sum() != arr2.sum()
        or not is_translatable(arr1)
        or not is_translatable(arr2)
    ):
        return False
    return any(
        np.array_equal(arr1, np.roll(arr2, (row_shift, col_shift), axis=(0, 1)))
        for row_shift in range(NB_ROWS)
        for col_shift in range(NB_COLS)
    )


def solve() -> None:
    print("computing the matrices...")
    matrices = {
        nb: int_to_numpy(nb) for nb in tqdm(range(2 ** (NB_COLS * NB_ROWS)))
    }  # caching
    print("computing the incompatibilities...")
    incompatibilities = set()
    for nb1 in tqdm(range(2 ** (NB_ROWS * NB_COLS))):
        if any(nb1 in group for group in incompatibilities):
            continue
        incompatibilities.add(
            frozenset(
                {nb1}
                | {
                    nb2
                    for nb2 in range(2 ** (NB_ROWS * NB_COLS))
                    if nb2 != nb1 and is_translation(*map(matrices.get, (nb1, nb2)))
                }
            )
        )
    print(f"Solution: {len(incompatibilities)}; {incompatibilities=}")


if __name__ == "__main__":
    solve()
