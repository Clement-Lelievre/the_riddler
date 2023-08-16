from random import choice


MODE = "CLASSIC"
# Riddler Express
# A digital 12-hour clock displays 10 digits: two digits representing the hour (from “00” to “12”),
# two digits representing the minute, two digits representing the second and four digits representing the year.
# When will the clock next use every digit from 0 to 9?


def find_time() -> str | None:
    """Find the next time the clock (see desc above) will use every digit from 0 to 9

    Returns:
        str | None: The best time if found, or None if no time was found
    """
    if MODE == "EXPRESS":
        for year in range(
            2_130, 9877
        ):  # 2130 is the minimum future year that has all 4 digits unique; 9876 is the largest such year
            year = str(year)
            for hour in ["0" + str(i) for i in range(1, 10)] + ["10", "12"]:
                for minutes in ["0" + str(i) for i in range(1, 10)] + [
                    str(i) for i in range(10, 60)
                ]:
                    for seconds in ["0" + str(i) for i in range(1, 10)] + [
                        str(i) for i in range(10, 60)
                    ]:
                        if len(set(year + hour + minutes + seconds)) == 10:
                            print((answer := year + hour + minutes + seconds))
                            return answer


# Riddler Classic
# From Anna Kómár comes a stumper about socks:
# In my laundry basket, I have 14 pairs of socks that I need to pair up. To do this, I use a chair that can fit nine socks, at most.
# I randomly draw one clean sock at a time from the basket. If its matching counterpart is not already on the chair, then
# I place it in one of the nine spots. But if its counterpart is already on the chair, then I remove it from the chair
# (making that spot once again unoccupied) and place the folded pair in my drawer.
# What is the probability I can fold all 14 pairs without ever running out of room on my chair?
# Extra credit: What if I change the number of pairs of socks I own, as well as the number of socks that can fit on my chair?


def simulate(f, nb_times: int = 100_000, verbose: bool = True):
    """Makes a simulation of the function f, `nb_times` times, and returns the proportion of times f returned True

    Args:
        f : the function to decorate
        nb_times (int, optional): Number of simulations. Defaults to 100_000.
        verbose (bool, optional): whether to print the probability of success. Defaults to True.

    Returns:
        f
    """
    if MODE == "CLASSIC":
        if verbose:
            print(f"Launching {nb_times} simulations of {f.__name__}...")
        proba = sum(f() for _ in range(nb_times)) / nb_times
        if verbose:
            print(f"{proba=}")
    return f


@simulate
def sort_socks(chair_capacity: int = 9, nb_socks_pairs: int = 14) -> bool | None:
    """Simulates the socks sorting described above

    Args:
        chair_capacity (int, optional): max capacity of the chair. Defaults to 9.
        nb_socks_pairs (int, optional): Number of socks pairs to sort. Defaults to 14.

    Raises:
        ValueError: if `chair_capacity`or `nb_socks_pairs` is not a positive integer

    Returns:
        bool: whether all socks pairs were sorted before the chair capacity was exceeded
    """
    if MODE == "CLASSIC":
        if (
            chair_capacity < 0
            or nb_socks_pairs < 0
            or not isinstance(chair_capacity, int)
            or not isinstance(nb_socks_pairs, int)
        ):
            raise ValueError(
                f"chair_capacity and nb_socks_pairs should be positive integers, you used: {chair_capacity=}, {nb_socks_pairs=}"
            )
        if chair_capacity >= nb_socks_pairs:
            return True
        on_chair = []
        socks = [
            i for i in range(nb_socks_pairs * 2)
        ]  # number the socks 0 to 27 included; pairings: 0-1 , 2-3 ... till 26-27
        while len(on_chair) <= chair_capacity:
            sock = choice(socks)  # randomly pick one sock from the socks pile
            on_chair.append(sock)  # add it to the chair
            socks.remove(sock)  # remove it to the socks pile
            if (
                counterpart := sock - 1 if sock % 2 else sock + 1
            ) in on_chair:  # if there's the matching sock on the chair
                on_chair.remove(sock)  # put matched sock in Anna's drawer
                on_chair.remove(counterpart)  # put matched sock in Anna's drawer
            if (
                not socks and not on_chair
            ):  # if both the chair and the pile are empty, it means we're done sorting socks
                return True
        return False


if __name__ == "__main__":
    find_time()
    sort_socks()

# TO DO if required: use multiprocessing to speed up the simulations, or use a better algorithm
