import pandas as pd

data = {"Level": [1, 2, 2, 3],
        "Name": ["Seat", "PP (polypropyleen)", "Screws", "Stainless steel"],
        "Quantity": [1, 2.4, 4, 0.1],
        "Unit": ["Items", "kg", "Items", "kg"]}
bom = pd.DataFrame(data=data)
levels = bom["Level"].values
quantity = bom["Quantity"].values


# Check if level 0 (product) is missing
def zero_level_missing(levels):
    if 0 in levels:
        return False
    else:
        return True


# Check if each element (besides the first) is maximum 1 greater than the previous element.
def validate_levels(levels):
    levels_valid = True
    for i in range(1, len(levels)):  # Start range at 1 because the first element can never be higher than the previous
        if levels[i] - levels[i-1] > 1:
            levels_valid = False
        else:
            continue
    return levels_valid


# Filter only the levels that ius greater or equal to the previous level
def match_level_indices(levels):
    match_indices = []
    for i in range(0, len(levels) - 1):
        if levels[i] < levels[i + 1]:
            pass
        else:
            match_indices.append(i)
    match_indices.append(len(levels))

    return match_indices


# Check if quantity has valid data type
def valid_quantity(row):
    if isinstance(row.Quantity, int):
        return True
    elif isinstance(row.Quantity, float):
        return True
    else:
        return False


# Check if unit has valid value
def valid_unit(row):
    if row.Unit in ['Kg', 'Items', 'm2']:
        return True
    else:
        return False

# -- UNIT TESTS --
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


# Unit test match_levels()
def test_match_level_indices():
    level = [1, 2, 3, 4]
    assert match_level_indices(level) == [4]


# Unit test match_levels()
def test_valid_quantity(bom):
    row = bom.loc[0]  #TODO: samenstellen
    assert valid_quantity(row)


test_validate_levels()
test_zero_level_missing()
test_match_level_indices()
test_valid_quantity(bom)

