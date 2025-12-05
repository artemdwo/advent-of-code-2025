from pathlib import Path


def get_data() -> list[list[str]]:
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "input.txt"

    with open(file_path, "r") as f:
        data = [list(line.rstrip("\n")) for line in f]
    return data


class Revisor:
    def __init__(self, grid: list[list[str]]):
        self.x_position = 0
        self.y_position = 0
        self.grid = grid
        self.x_max = len(grid[0]) - 1
        self.y_max = len(grid) - 1
        self.rolls_count = 0
        self.empty_spots = "."
        self.a_roll = "@"

    def more_rolls(self):
        self.rolls_count += 1

    def how_many_rools(self) -> int:
        return self.rolls_count

    def move_right(self, steps: int = 1):
        self.x_position += steps

    def move_down(self, steps: int = 1):
        self.y_position += steps

    def lookaround(self):
        self.neighbours_count = 0
        x = self.x_position
        y = self.y_position
        if self.grid[y][x] == self.a_roll:
            if y - 1 >= 0 and x - 1 >= 0 and self.grid[y - 1][x - 1] == self.a_roll:
                self.neighbours_count += 1
            if y - 1 >= 0 and self.grid[y - 1][x] == self.a_roll:
                self.neighbours_count += 1

            if (
                y + 1 <= self.y_max
                and x - 1 >= 0
                and self.grid[y + 1][x - 1] == self.a_roll
            ):
                self.neighbours_count += 1
            if x - 1 >= 0 and self.grid[y][x - 1] == self.a_roll:
                self.neighbours_count += 1

            if (
                y - 1 >= 0
                and x + 1 <= self.x_max
                and self.grid[y - 1][x + 1] == self.a_roll
            ):
                self.neighbours_count += 1
            if x + 1 <= self.x_max and self.grid[y][x + 1] == self.a_roll:
                self.neighbours_count += 1

            if (
                y + 1 <= self.y_max
                and x + 1 <= self.x_max
                and self.grid[y + 1][x + 1] == self.a_roll
            ):
                self.neighbours_count += 1
            if y + 1 <= self.y_max and self.grid[y + 1][x] == self.a_roll:
                self.neighbours_count += 1
        return

    def is_it_moveable(self) -> bool:
        if self.grid[self.y_position][self.x_position] != self.a_roll:
            self.neighbours_count = 0
            return False

        if self.neighbours_count >= 4:
            self.neighbours_count = 0
            return False
        self.neighbours_count = 0
        return True


def find_rolls_to_unload() -> int:
    grid = get_data()
    revisor = Revisor(grid)
    while revisor.y_position <= revisor.y_max:
        while revisor.x_position <= revisor.x_max:
            revisor.lookaround()
            if revisor.is_it_moveable():
                revisor.more_rolls()
            revisor.move_right()
        revisor.x_position = 0
        revisor.move_down()
    return revisor.how_many_rools()


if __name__ == "__main__":
    print(find_rolls_to_unload())
