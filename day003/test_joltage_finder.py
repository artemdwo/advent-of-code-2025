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
def test_find_max_joltage_simple_cases_pos():
    assert joltage_finder.find_max_joltage("12") == 12
    assert joltage_finder.find_max_joltage("34") == 34
    assert joltage_finder.find_max_joltage("56") == 56


def test_find_max_joltage_multiple_digits_pos():
    assert joltage_finder.find_max_joltage("123") == 23
    assert joltage_finder.find_max_joltage("456") == 56
    assert joltage_finder.find_max_joltage("789") == 89


def test_find_max_joltage_simple_cases_neg():
    assert joltage_finder.find_max_joltage("12") != 21
    assert joltage_finder.find_max_joltage("34") != 43
    assert joltage_finder.find_max_joltage("56") != 65


def test_find_max_joltage_multiple_digits_neg():
    assert joltage_finder.find_max_joltage("123") != 32
    assert joltage_finder.find_max_joltage("456") != 65
    assert joltage_finder.find_max_joltage("789") != 98


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
    expected_sum = 98 + 89 + 78 + 92
    assert result == expected_sum


def test_find_total_joltage_no_banks(monkeypatch):
    fake_banks = []

    def fake_get_data():
        return fake_banks

    monkeypatch.setattr(joltage_finder, "get_data", fake_get_data)

    result = joltage_finder.find_total_joltage()
    expected_sum = 0
    assert result == expected_sum
