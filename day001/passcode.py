from pathlib import Path

START = 50


def get_data():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "input.txt"

    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


class CodeDial:
    def __init__(self):
        self.value = START

    def currently_at(self) -> int:
        return self.value

    def move_right(self) -> int:
        self.value += 1
        return self.value

    def move_left(self) -> int:
        self.value -= 1
        return self.value

    def is_0(self) -> bool:
        return self.value == 0

    def is_99(self) -> bool:
        return self.value == 99

    def rollover_99(self):
        if self.is_99():
            self.value = 0

    def rollover_0(self):
        if self.is_0():
            self.value = 99


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self) -> int:
        return self.count


def find_pass() -> int:
    spinner = CodeDial()
    num_zeros = Counter()
    RTTS = get_data()

    while True:
        for move in RTTS:
            # print(move)
            direction = move[0]
            steps = int(move[1:])

            if direction == "R":
                while steps > 0:
                    if spinner.is_99():
                        spinner.rollover_99()
                        steps -= 1
                    else:
                        spinner.move_right()
                        steps -= 1

            if direction == "L":
                while steps > 0:
                    if spinner.is_0():
                        spinner.rollover_0()
                        steps -= 1
                    else:
                        spinner.move_left()
                        steps -= 1
            if spinner.is_0():
                num_zeros.increment()

        return num_zeros.get_count()


if __name__ == "__main__":
    print(find_pass())
