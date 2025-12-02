from pathlib import Path
from typing import Generator


def get_data():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "input.txt"

    with open(file_path, "r") as f:
        data = f.read().split(",")
    return data


class TheTotal:
    def __init__(self):
        self.count = 0

    def increase(self, amount: int):
        self.count += amount

    def get_count(self) -> int:
        return self.count


def parse_data(ranges: list[str]) -> Generator[tuple[int, int], None, None]:
    for part in ranges:
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        yield int(start_str), int(end_str)


def is_invalid(id: int) -> bool:
    s = str(id)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    left = s[:half]
    right = s[half:]

    return left == right


def find_invalid_ids() -> int:
    result = TheTotal()
    product_ids_raw = get_data()

    for range_start, range_end in parse_data(product_ids_raw):
        for id in range(range_start, range_end + 1):
            if is_invalid(id):
                result.increase(id)
    return result.get_count()


if __name__ == "__main__":
    print(find_invalid_ids())
