# Check if level 0 (product) is present
def zero_level_present(levels):
    if 0 in levels:
        return True
    else:
        return False


# Check if each element (besides the first) is maximum 1 greater than the previous element.
def validate_levels(levels):
    levels_valid = True
    # print(levels)
    for i in range(1, len(levels)):  # Start range at 1 because the first element can never be higher than the previous
        if levels[i] - levels[i-1] > 1:
            levels_valid = False
        else:
            continue
    return levels_valid


# Filter only the levels that are greater or equal to the previous level
def match_level_indices(levels):
    match_indices = []
    for i in range(0, len(levels) - 1):
        if levels[i] < levels[i + 1]:
            pass
        else:
            match_indices.append(i)
    match_indices.append(len(levels)-1)

    return match_indices


# Check if quantity has valid data type
def valid_quantity(row):
    if isinstance(row.Quantity, (int, float)):
        return True
    else:
        return False


# Check if unit has valid value
def valid_unit(row):
    if row.Unit in ['kg', 'Items', 'm2']:
        return True
    else:
        return False


# -- UNIT TESTS --
# Unit test zero_level_missing()
def test_zero_level_present():
    invalid_levels = [1, 2, 3, 4, 5]
    valid_levels = [0, 1, 3, 3, 4]
    assert zero_level_present(valid_levels) and not zero_level_present(invalid_levels)


# Unit test validate_levels()
def test_validate_levels():
    valid_levels = [1, 2, 3, 4, 5]
    invalid_levels = [1, 3, 3, 4, 5]
    assert validate_levels(valid_levels) and not validate_levels(invalid_levels)


# Unit test match_levels()
def test_match_level_indices():
    level = [1, 2, 3, 3]
    assert match_level_indices(level) == [2, 3]


# Execute all unit tests
def execute_unit_tests():
    test_validate_levels()
    test_zero_level_present()
    test_match_level_indices()