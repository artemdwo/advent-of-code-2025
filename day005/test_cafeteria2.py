import pytest

from cafeteria2 import get_fresh_data, find_all_fresh_ingridients, merge_ranges


@pytest.fixture
def setup_test_files(tmp_path, monkeypatch):
    fresh_file = tmp_path / "fresh_ids.txt"
    fresh_file.write_text("3-5\n10-14\n16-20\n12-18\n")

    class DummyFile:
        __file__ = str(tmp_path / "dummy.py")

    monkeypatch.setattr("cafeteria2.__file__", DummyFile.__file__)

    return tmp_path


def test_get_fresh_data(setup_test_files):
    expected = [
        (3, 5),
        (10, 14),
        (16, 20),
        (12, 18),
    ]
    assert get_fresh_data() == expected


def test_merge_ranges(monkeypatch):
    mock_fresh_data = [
        (3, 5),
        (10, 14),
        (16, 20),
        (12, 18),
    ]

    expected = [(3, 5), (10, 20)]

    result = merge_ranges(mock_fresh_data)
    assert result == expected


def test_find_all_fresh_ingridients(monkeypatch):
    mock_fresh_data = [
        (3, 5),
        (10, 14),
        (16, 20),
        (12, 18),
    ]

    monkeypatch.setattr("cafeteria2.get_fresh_data", lambda: mock_fresh_data)

    result = find_all_fresh_ingridients()
    assert result == 14
