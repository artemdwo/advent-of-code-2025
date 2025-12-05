import pytest

from cafeteria import (
    get_fresh_data,
    get_availability_data,
    is_it_fresh,
    find_fresh_ingridients,
)


@pytest.fixture
def setup_test_files(tmp_path, monkeypatch):
    fresh_file = tmp_path / "fresh_ids.txt"
    fresh_file.write_text("3-5\n10-14\n16-20\n12-18\n")

    available_file = tmp_path / "available_ids.txt"
    available_file.write_text("1\n5\n8\n11\n17\n32\n")

    class DummyFile:
        __file__ = str(tmp_path / "dummy.py")

    monkeypatch.setattr("cafeteria.__file__", DummyFile.__file__)

    return tmp_path


def test_get_fresh_data(setup_test_files):
    expected = [
        [3, 5],
        [10, 14],
        [16, 20],
        [12, 18],
    ]
    assert get_fresh_data() == expected


def test_get_availability_data(setup_test_files):
    expected = [1, 5, 8, 11, 17, 32]
    assert get_availability_data() == expected


def test_is_it_fresh_is_false():
    fresh_ids = [
        [3, 5],
        [10, 14],
        [16, 20],
        [12, 18],
    ]
    assert is_it_fresh(fresh_ids, 1) is False


def test_is_it_fresh_is_true():
    fresh_ids = [
        [3, 5],
        [10, 14],
        [16, 20],
        [12, 18],
    ]
    assert is_it_fresh(fresh_ids, 11) is True


def test_find_fresh_ingridients(monkeypatch):
    mock_fresh_data = [
        [3, 5],
        [10, 14],
        [16, 20],
        [12, 18],
    ]

    mock_available_data = [1, 5, 8, 11, 17, 32]

    monkeypatch.setattr("cafeteria.get_fresh_data", lambda: mock_fresh_data)

    monkeypatch.setattr("cafeteria.get_availability_data", lambda: mock_available_data)

    result = find_fresh_ingridients()
    assert result == 3
