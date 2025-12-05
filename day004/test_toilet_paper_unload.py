import pytest
import toilet_paper_unload 
from toilet_paper_unload import Revisor, find_rolls_to_unload

GRID_TEXT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def make_grid(text: str):
    """Helper: convert multiline string into list[list[str]]."""
    return [list(line) for line in text.splitlines()]


@pytest.fixture
def grid():
    return make_grid(GRID_TEXT)


@pytest.fixture
def revisor_obj(grid):
    return Revisor(grid)


def test_is_it_moveable_accessible_roll(revisor_obj):
    """
    Position (row=0, col=2) is an accessible roll in the example:
    original row 0:  ..@@.@@@@.
    solution row 0:  ..xx.xx@x.

    We expect this to be moveable (True).
    """
    revisor_obj.y_position = 0
    revisor_obj.x_position = 2

    revisor_obj.lookaround()
    assert revisor_obj.is_it_moveable() is True


def test_is_it_moveable_blocked_roll(revisor_obj):
    """
    Position (row=2, col=0) is NOT accessible in the example:
    original row 2:  @@@@@.@.@@
    solution row 2:  @@@@@.x.@@

    We expect this to be NOT moveable (False).
    """
    revisor_obj.y_position = 2
    revisor_obj.x_position = 0

    revisor_obj.lookaround()
    assert revisor_obj.is_it_moveable() is False


def test_is_it_moveable_empty_cell_is_never_moveable(revisor_obj):
    """
    An empty cell ('.') should never be considered moveable,
    even if it has few neighbours.
    For example, (row=0, col=0) is '.'.
    """
    revisor_obj.y_position = 0
    revisor_obj.x_position = 0

    revisor_obj.lookaround()
    assert revisor_obj.is_it_moveable() is False


def test_is_it_moveable_resets_neighbour_count(revisor_obj):
    """
    After calling is_it_moveable(), neighbours_count should be reset
    back to 0 so it doesn't leak into the next check.
    """
    revisor_obj.y_position = 0
    revisor_obj.x_position = 2

    revisor_obj.lookaround()
    _ = revisor_obj.is_it_moveable()
    assert revisor_obj.neighbours_count == 0


def test_find_rolls_to_unload_uses_example_grid(monkeypatch):
    """
    Use the example grid by monkeypatching get_data() so we don't need a file.

    According to the puzzle statement, there are 13 accessible rolls.
    """
    grid = make_grid(GRID_TEXT)

    def fake_get_data():
        return grid

    monkeypatch.setattr(toilet_paper_unload, "get_data", fake_get_data)

    result = find_rolls_to_unload()
    assert result == 13
