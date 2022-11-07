import plotly.graph_objects as go

# The end of daylight saving time here on the East Coast of the U.S. got me thinking more generally about the calendar year.
# Each solar year consists of approximately 365.24217 mean solar days. That’s pretty close to 365.25, which is why it makes sense
# to have an extra day every four years. However, the Gregorian calendar is a little more precise: There are 97 leap years every 400 years,
# averaging out to 365.2425 days per year.

# Can you make a better approximation than the Gregorian calendar? Find numbers L and N (where N is less than 400) such that if
# every cycle of N years includes L leap years, the average number of days per year is as close as possible to 365.24217.


# intuitive approach
best_l, best_n = 0, 0
target = 365.24217
gap = 10**100  # an arbitrarily large number
fractions_processed = set()
for n in range(1, 401):
    for l in range(1, n + 1):
        if (
            frac := l / n
        ) not in fractions_processed:  # discard duplicated values for time efficiency (~40% drop in nb of iterations!)
            fractions_processed.add(frac)
            avg_days_per_year = (l * 366 + (n - l) * 365) / n
            if (current_gap := abs(avg_days_per_year - target)) < gap:
                best_l = l
                best_n = n
                gap = current_gap
print(f"{(best_l*366 + (best_n - best_l)*365)/best_n=}", best_l, best_n)


# pythonic, more compact version using a generator for space efficiency
answer = min(
    ((l, n) for n in range(1, 401) for l in range(1, n + 1)),
    key=lambda data, target=365.24217: abs(
        (data[0] * 366 + (data[1] - data[0]) * 365) / data[1] - target
    ),
)

print(*answer)

# graphing the 3D surface showing all possible combinations (real-valued)
def year_in_days(nb_leap_years: int, cycle_length: int) -> float:
    """Computes the exact number of days in a year in a scenario with `nb_leap_years` in `cycle_length` years"""
    return (
        (nb_leap_years * 366 + (cycle_length - nb_leap_years) * 365) / cycle_length
        if nb_leap_years <= cycle_length
        else 0
    )


# x, y = list(range(1, 400)), list(range(1, 400))
# fig = go.Figure(
#     data=[
#         go.Scatter3d(
#             x=x,
#             y=y,
#             z=[
#                 year_in_days(nb_leap_years, cycle_length)
#                 for nb_leap_years in x
#                 for cycle_length in y
#             ],
#         )
#     ]
# )

# fig.show()
