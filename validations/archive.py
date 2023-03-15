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