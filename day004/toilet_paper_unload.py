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

    def lookaround(self):
        self.neighbours_count = 0

        if self.grid[self.y_position][self.x_position] != self.a_roll:
            return

        y = self.y_position
        x = self.x_position

        # top row neighbours
        if y - 1 >= 0 and x - 1 >= 0 and self.grid[y - 1][x - 1] == self.a_roll:
            self.neighbours_count += 1
        if y - 1 >= 0 and self.grid[y - 1][x] == self.a_roll:
            self.neighbours_count += 1
        if (
            y - 1 >= 0
            and x + 1 <= self.x_max
            and self.grid[y - 1][x + 1] == self.a_roll
        ):
            self.neighbours_count += 1

        # same row neighbours
        if x - 1 >= 0 and self.grid[y][x - 1] == self.a_roll:
            self.neighbours_count += 1
        if x + 1 <= self.x_max and self.grid[y][x + 1] == self.a_roll:
            self.neighbours_count += 1

        # bottom row neighbours
        if (
            y + 1 <= self.y_max
            and x - 1 >= 0
            and self.grid[y + 1][x - 1] == self.a_roll
        ):
            self.neighbours_count += 1
        if y + 1 <= self.y_max and self.grid[y + 1][x] == self.a_roll:
            self.neighbours_count += 1
        if (
            y + 1 <= self.y_max
            and x + 1 <= self.x_max
            and self.grid[y + 1][x + 1] == self.a_roll
        ):
            self.neighbours_count += 1

    def is_it_moveable(self) -> bool:
        if self.grid[self.y_position][self.x_position] != self.a_roll:
            self.neighbours_count = 0
            return False

        moveable = self.neighbours_count < 4
        self.neighbours_count = 0
        return moveable


def find_rolls_to_unload() -> int:
    grid = get_data()
    revisor = Revisor(grid)

    for y in range(revisor.y_max + 1):
        for x in range(revisor.x_max + 1):
            revisor.y_position = y
            revisor.x_position = x
            revisor.lookaround()
            if revisor.is_it_moveable():
                revisor.more_rolls()

    return revisor.how_many_rools()


def find_total_rolls_removed() -> int:
    grid = get_data()
    revisor = Revisor(grid)
    total_removed = 0

    while True:
        removable_positions = []

        for y in range(revisor.y_max + 1):
            for x in range(revisor.x_max + 1):
                revisor.y_position = y
                revisor.x_position = x
                revisor.lookaround()
                if revisor.is_it_moveable():
                    removable_positions.append((y, x))

        if not removable_positions:
            break

        for y, x in removable_positions:
            grid[y][x] = revisor.empty_spots

        total_removed += len(removable_positions)

    return total_removed


if __name__ == "__main__":
    print("Accessible rolls on the first go:", find_rolls_to_unload())
    print("Total rolls removed over all iterations:", find_total_rolls_removed())
