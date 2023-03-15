import pandas as pd

bom = {'Level': [1, 2, 2, 3], 'Name': ['Seat', 'PP (polypropyleen)', 'Screws', 'Stainless steel']}
df_bom = pd.DataFrame(data=bom)


# Check if level 0 (product) is missing
def zero_level_missing(levels):
    if 0 in levels:
        return False
    else:
        return True


# Check if each element (besides the first) is maximum 1 greater than the previous element.
def validate_levels(levels):
    levels_valid = True
    for i in range(1, len(levels)):
        if levels[i] - levels[i-1] > 1:
            levels_valid = False
        else:
            continue
    return levels_valid


# Unit test validate_levels()
def test_validate_levels():
    valid_levels = [1, 2, 3, 4, 5]
    invalid_levels = [1, 3, 3, 4, 5]
    assert validate_levels(valid_levels) and not validate_levels(invalid_levels)


# Unit test validate_levels()
def test_zero_level_missing():
    valid_levels = [1, 2, 3, 4, 5]
    invalid_levels = [0, 1, 3, 3, 4]
    assert zero_level_missing(valid_levels) and not zero_level_missing(invalid_levels)
