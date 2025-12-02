import passcode


# CodeDial
def test_code_dial_starts_at_start_constant():
    spinner = passcode.CodeDial()
    assert spinner.currently_at() == passcode.START


def test_code_dial_move_right_and_left():
    spinner = passcode.CodeDial()

    spinner.move_right()
    assert spinner.currently_at() == passcode.START + 1

    spinner.move_left()
    assert spinner.currently_at() == passcode.START


def test_code_dial_rollover_99_to_0():
    spinner = passcode.CodeDial()
    while not spinner.is_99():
        spinner.move_right()

    assert spinner.currently_at() == 99
    spinner.rollover_99()
    assert spinner.currently_at() == 0


def test_code_dial_rollover_0_to_99():
    spinner = passcode.CodeDial()
    while not spinner.is_0():
        spinner.move_left()

    assert spinner.currently_at() == 0
    spinner.rollover_0()
    assert spinner.currently_at() == 99


def test_rollover_99_does_nothing_if_not_99():
    spinner = passcode.CodeDial()
    spinner.value = 98
    spinner.rollover_99()
    assert spinner.currently_at() == 98


def test_rollover_0_does_nothing_if_not_0():
    spinner = passcode.CodeDial()
    spinner.value = 1
    spinner.rollover_0()
    assert spinner.currently_at() == 1


# Counter
def test_counter_starts_at_zero():
    c = passcode.Counter()
    assert c.get_count() == 0


def test_counter_increments():
    c = passcode.Counter()
    c.increment()
    c.increment()
    assert c.get_count() == 2


# find_pass
def test_find_pass_never_hits_zero(monkeypatch):
    fake_moves = ["R1", "L1", "R10"]

    def fake_get_data():
        return fake_moves

    monkeypatch.setattr(passcode, "get_data", fake_get_data)

    result = passcode.find_pass()
    assert result == 0


def test_find_pass_hits_zero_once_right(monkeypatch):
    fake_moves = ["R50"]

    def fake_get_data():
        return fake_moves

    monkeypatch.setattr(passcode, "get_data", fake_get_data)

    result = passcode.find_pass()
    assert result == 1


def test_find_pass_hits_zero_once_left(monkeypatch):
    fake_moves = ["L50"]

    def fake_get_data():
        return fake_moves

    monkeypatch.setattr(passcode, "get_data", fake_get_data)

    result = passcode.find_pass()
    assert result == 1


def test_find_pass_complex_sequence(monkeypatch):
    fake_moves = ["R25", "R25", "R50"]

    def fake_get_data():
        return fake_moves

    monkeypatch.setattr(passcode, "get_data", fake_get_data)

    result = passcode.find_pass()
    assert result == 1


def test_find_pass_does_not_count_mid_move_zero(monkeypatch):
    fake_moves = ["R51"]

    def fake_get_data():
        return fake_moves

    monkeypatch.setattr(passcode, "get_data", fake_get_data)

    result = passcode.find_pass()
    assert result == 0


def test_find_pass_advent_of_code_sequence(monkeypatch):
    fake_moves = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    def fake_get_data():
        return fake_moves

    monkeypatch.setattr(passcode, "get_data", fake_get_data)

    result = passcode.find_pass()
    assert result == 3
