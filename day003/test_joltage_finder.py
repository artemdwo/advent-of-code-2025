import joltage_finder


# Counter
def test_counter_starts_at_zero():
    c = joltage_finder.TheTotal()
    assert c.get_count() == 0


def test_counter_increments():
    c = joltage_finder.TheTotal()
    c.increase(5)
    assert c.get_count() == 5
    c.increase(10)
    assert c.get_count() == 15


# find_max_joltage
def test_find_max_joltage_multiple_digits_pos():
    assert joltage_finder.find_max_joltage("987654321111111") == 987654321111
    assert joltage_finder.find_max_joltage("811111111111119") == 811111111119
    assert joltage_finder.find_max_joltage("234234234234278") == 434234234278


def test_find_max_joltage_multiple_digits_neg():
    assert joltage_finder.find_max_joltage("987654322111111") != 987654321111
    assert joltage_finder.find_max_joltage("821111111111119") != 811111111119
    assert joltage_finder.find_max_joltage("235234234234278") != 434234234278


# find_total_joltage
def test_find_total_joltage_advent_case(monkeypatch):
    fake_banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    def fake_get_data():
        return fake_banks

    monkeypatch.setattr(joltage_finder, "get_data", fake_get_data)

    result = joltage_finder.find_total_joltage()
    expected_sum = 987654321111 + 811111111119 + 434234234278 + 888911112111
    assert result == expected_sum


def test_find_total_joltage_no_banks(monkeypatch):
    fake_banks = []

    def fake_get_data():
        return fake_banks

    monkeypatch.setattr(joltage_finder, "get_data", fake_get_data)

    result = joltage_finder.find_total_joltage()
    expected_sum = 0
    assert result == expected_sum
