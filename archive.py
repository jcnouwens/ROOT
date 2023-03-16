import time
import pandas as pd

start = time.perf_counter()
end = time.perf_counter()
print(end - start)

data = {"Level": [1, 2, 2, 3],
        "Name": ["Seat", "PP (polypropyleen)", "Screws", "Stainless steel"],
        "Quantity": [1, 2.4, 4, 0.1],
        "Unit": ["Items", "kg", "Items", "kg"]}
bom = pd.DataFrame(data=data)


# Filter only the levels that ius greater or equal to the previous level
def match_levels(levels):
    match_bool = []
    for i in range(0, len(levels) - 1):
        if levels[i] < levels[i + 1]:
            match_bool.append(False)
        else:
            match_bool.append(True)
    match_bool.append(True)

    return match_bool


# Unit test match_levels()
def test_match_levels():
    levels = [1, 2, 3, 4]
    assert match_levels(levels) == [False, False, False, True]


# Unit test match_levels()
def test_valid_quantity(bom):
    row = bom.loc[0]
    assert valid_quantity(row)
