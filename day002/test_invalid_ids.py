import invalid_ids


# Counter
def test_counter_starts_at_zero():
    c = invalid_ids.TheTotal()
    assert c.get_count() == 0


def test_counter_increments():
    c = invalid_ids.TheTotal()
    c.increase(5)
    assert c.get_count() == 5
    c.increase(10)
    assert c.get_count() == 15


# parse_data
def test_parse_data_yields_correct_tuples():
    input_data = ["1-5", "10-15", "20-25"]
    expected_output = [(1, 5), (10, 15), (20, 25)]

    result = list(invalid_ids.parse_data(input_data))
    assert result == expected_output


def test_parse_data_yields_correct_tuples_no_leading_zeros():
    input_data = ["01-05", "010-15", "020-025"]
    expected_output = [(1, 5), (10, 15), (20, 25)]

    result = list(invalid_ids.parse_data(input_data))
    assert result == expected_output


# is_invalid
def test_is_invalid_even_length_invalid():
    assert invalid_ids.is_invalid(1212) is True
    assert invalid_ids.is_invalid(123123) is True
    assert invalid_ids.is_invalid(99999999) is True


def test_is_invalid_even_length_valid():
    assert invalid_ids.is_invalid(1234) is False
    assert invalid_ids.is_invalid(123456) is False
    assert invalid_ids.is_invalid(12349999) is False


def test_is_invalid_odd_length():
    assert invalid_ids.is_invalid(123) is False
    assert invalid_ids.is_invalid(12345) is False
    assert invalid_ids.is_invalid(1234567) is False


# find_invalid_ids
def test_find_invalid_ids_advent_case(monkeypatch):
    fake_range = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 1227775554
    assert result == expected_sum


def test_find_invalid_ids(monkeypatch):
    fake_range = ["10-15", "20-25"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 11 + 22
    assert result == expected_sum


def test_find_invalid_ids_all_invalids(monkeypatch):
    fake_range = ["11-11", "22-22", "1212-1212"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 11 + 22 + 1212
    assert result == expected_sum


def test_find_invalid_ids_with_leading_zeros(monkeypatch):
    fake_range = ["01-05", "10-15"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 11
    assert result == expected_sum


def test_find_invalid_ids_large_range(monkeypatch):
    fake_range = ["1000-1020"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 1010
    assert result == expected_sum


def test_find_invalid_ids_single_number_ranges(monkeypatch):
    fake_range = ["11-22", "12-12", "22-22", "33-33"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 11 + 22 + 22 + 33
    assert result == expected_sum


def test_find_invalid_ids_mixed_ranges(monkeypatch):
    fake_range = ["5-15", "20-30", "100-110"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 11 + 22
    assert result == expected_sum


def test_find_invalid_ids_no_ranges(monkeypatch):
    fake_range = ["", "   ", "\n"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 0
    assert result == expected_sum


def test_find_invalid_ids_empty_input(monkeypatch):
    fake_range = []

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 0
    assert result == expected_sum


def test_find_invalid_ids_no_invalids(monkeypatch):
    fake_range = ["1-9", "100-199"]

    def fake_get_data():
        return fake_range

    monkeypatch.setattr(invalid_ids, "get_data", fake_get_data)

    result = invalid_ids.find_invalid_ids()
    expected_sum = 0
    assert result == expected_sum
